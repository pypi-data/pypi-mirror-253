from typing import TYPE_CHECKING, Any, Iterable

import einops
import numpy as np
import torch
from iot_rl_env.base_env import BaseEnv
from iot_rl_env.project_typing import ObservationType, RewardType
from iot_rl_model.common.base_module import BaseModule
from lightning.pytorch.utilities.types import STEP_OUTPUT
from tensordict import TensorDict  # type:ignore[import]
from torch import nn
from torch.distributions import Normal
from transformers.modeling_utils import Conv1D  # type: ignore[import]

from .config_class import DTContinuousConfig
from .context import init_context, update_context
from .dataset import DTDataset
from .dt import Block

if TYPE_CHECKING:
    from .dataset import Sample

MODALITIES = 3  # reward_to_go, observation, action
MASK_BIAS = -1e4  # values to overwrite masked values with


class OnlineDT(BaseModule[DTContinuousConfig]):
    """Concise implementation of Offline Decision Transformers.

    einops is a library used to manipulate tensor shapes.
    Here, the keys refer to:
    b: batch size
    m: number of modalities (3 in our case: observations, rewards, actions)
    c: context length (number of steps in the context)
    e: embedding dimension
    h: number of heads in the multi-head attention
    """

    def __init__(self, cfg: DTContinuousConfig) -> None:
        super().__init__(cfg)
        self.dataset = DTDataset(
            self.env,
            self.cfg.n_samples,
            self.cfg.context_length,
            self.cfg.batch_size,
            self.cfg.batches_per_epoch,
        )
        self.automatic_optimization = False

    def build_networks(self) -> None:
        self.layer_norm = nn.LayerNorm(self.cfg.embed_dim)
        self.dropout = nn.Dropout(self.cfg.dropout)
        self.blocks: Iterable[Block] = nn.ModuleList(
            [
                Block(self.cfg.embed_dim, self.cfg.n_head, self.cfg.dropout, MODALITIES * self.cfg.context_length)
                for _ in range(self.cfg.n_layer)
            ],
        )
        self.mean_layer = nn.Linear(self.cfg.embed_dim, self.cfg.action_dim)
        self.log_std_layer = nn.Linear(self.cfg.embed_dim, self.cfg.action_dim)
        self.apply(self._init_weights)  # paper doesn't init following embeddings layers
        self.embed_timestep = nn.Embedding(self.env.max_episode_steps, self.cfg.embed_dim)  # try padding_idx == 0
        self.embed_return = torch.nn.Linear(1, self.cfg.embed_dim)
        self.embed_observation = torch.nn.Linear(self.cfg.state_dim, self.cfg.embed_dim)
        self.embed_action = torch.nn.Linear(self.cfg.action_dim, self.cfg.embed_dim)
        self.embed_layer_norm = nn.LayerNorm(self.cfg.embed_dim)

        self.target_entropy = 0.1
        self.log_temperature = torch.tensor(np.log(self.target_entropy), requires_grad=True)

    def _init_weights(self, module: nn.Module) -> None:
        """Initialize the weights."""
        if isinstance(module, (nn.Embedding, Conv1D)):
            module.weight.data.normal_(std=0.02)
            if isinstance(module, (Conv1D)) and module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)
        elif isinstance(module, torch.nn.Linear):
            nn.init.orthogonal_(module.weight.data)  # type:ignore[no-untyped-call]
            if module.bias is not None:
                module.bias.data.zero_()

    def training_step(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        batch = self.dataset.sample()
        actions = batch["actions"][batch["mask"].squeeze(-1)]
        hidden_state = self.forward(batch)[batch["mask"].squeeze(-1)]

        mean = self.mean_layer(hidden_state)  # why no activation function here?
        log_std = self.log_std_layer(hidden_state)  # We output the log_std to ensure that std=exp(log_std)>0
        log_std = torch.clamp(log_std, -20, 2)

        dist = Normal(mean, log_std.exp())  # type: ignore[no-untyped-call]
        log_pi = dist.log_prob(actions).sum(dim=1).mean()  # type: ignore[no-untyped-call]
        entropy = dist.entropy().mean()  # type: ignore[no-untyped-call]

        actor_loss = -(log_pi + self.log_temperature.exp().detach() * entropy)

        actor_loss = -log_pi.mean()
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.parameters(), 0.25, error_if_nonfinite=True)
        self.actor_optimizer.step()

        temperature_loss = self.log_temperature.exp() * (entropy - self.target_entropy).detach()
        self.temperature_optimizer.zero_grad()
        temperature_loss.backward()
        self.temperature_optimizer.step()
        return {
            "actor_loss": actor_loss,
            "mean": mean.mean(),
            "std": log_std.exp().mean(),
            "entropy": entropy,
            "log_pi": log_pi,
            "temperature_loss": temperature_loss,
            "temperature": self.log_temperature.exp(),
        }

    def forward(self, batch: TensorDict) -> torch.Tensor:  # type: ignore[override]
        # embed each modality with a different head
        # time embeddings are treated similar to positional embeddings
        time_embeddings = self.embed_timestep(batch["timesteps"].squeeze(-1))
        observation_embeddings = self.embed_observation(batch["observations"]) + time_embeddings
        action_embeddings = self.embed_action(batch["actions"]) + time_embeddings
        returns_embeddings = self.embed_return(batch["reward_to_gos"]) + time_embeddings

        # [[r0...rn], [s0...sn], [a0...an]] -> (r0, s0, a0, r1, s1, a1, ...)
        stacked_inputs = einops.rearrange(
            [returns_embeddings, observation_embeddings, action_embeddings],
            "m b c e -> b (c m) e",
        )
        inputs_embeds = self.embed_layer_norm(stacked_inputs)

        # to make the attention mask fit the stacked inputs, have to stack it as well
        mask = einops.repeat(batch["mask"], "b c 1 -> b 1 1 (c m)", m=MODALITIES)
        hidden_states = self.dropout(inputs_embeds)
        for block in self.blocks:
            hidden_states = block.forward(
                hidden_states,
                mask=mask,
            )
        hidden_state = self.layer_norm(hidden_states)
        # reshape x so that the second dimension corresponds to the original
        hidden_state = einops.rearrange(hidden_state, "b (c m) e-> b m c e", m=MODALITIES)
        # [:, 1] selects the hidden state of the observation modality
        return hidden_state[:, 1]

    def normalize_observation(self, obs: ObservationType) -> torch.Tensor:  # type: ignore[override]
        return (torch.from_numpy(obs).float() - self.dataset.observation_mean) / (self.dataset.observation_std + 1e-6)

    def init_episode(self, env: BaseEnv, target_reward: RewardType) -> TensorDict:
        obs, _ = env.reset()
        context = init_context(
            self.cfg.context_length,
            self.cfg.state_dim,
            self.cfg.action_dim,
        )
        update_context(
            context,
            target_reward,
            self.normalize_observation(obs),
            torch.zeros(self.cfg.action_dim, dtype=torch.float32),
        )
        return context

    def self_play_step(  # type: ignore[override]
        self,
        env: BaseEnv,
        context: TensorDict,
        target_rew: RewardType,
        *,
        deterministic: bool,
    ) -> "Sample":
        hidden_state = self.forward(context.unsqueeze(0))[0, -1]  # 1 batch here, extract last action
        if deterministic:
            action = self.mean_layer(hidden_state)
        else:
            mean = self.mean_layer(hidden_state)
            log_std = self.log_std_layer(hidden_state)
            log_std = torch.clamp(log_std, -20, 2)
            dist = Normal(mean, log_std.exp())  # type:ignore[no-untyped-call]# Generate a Gaussian distribution
            action = dist.sample()  # type:ignore[no-untyped-call]
        action = torch.clamp(action, self.cfg.min_action, self.cfg.max_action)
        context["actions"][-1] = action
        obs, reward, _, _, _ = env.step(action.numpy())
        obs = self.normalize_observation(obs)  # type:ignore[assignment]
        update_context(
            context,
            target_rew - env.episode_reward,
            obs,  # type: ignore[arg-type]
            torch.zeros(self.cfg.action_dim, dtype=torch.float32),
        )
        return (reward, obs, action)

    @torch.no_grad()
    def self_play_episode(self) -> None:
        target_reward = self.dataset.max_reward * 1.1
        samples = TensorDict(
            {
                "observations": torch.empty((self.env.horizon + 1, self.cfg.context_length, self.cfg.state_dim)),
                "actions": torch.empty((self.env.horizon + 1, self.cfg.context_length, self.cfg.action_dim)),
                "reward_to_gos": torch.empty((self.env.horizon + 1, self.cfg.context_length, 1)),
                "timesteps": torch.empty((self.env.horizon + 1, self.cfg.context_length, 1), dtype=torch.int64),
                "mask": torch.empty((self.env.horizon + 1, self.cfg.context_length, 1), dtype=torch.bool),
            },
            batch_size=(self.env.horizon + 1, self.cfg.context_length),
        )
        context = self.init_episode(self.env, target_reward)
        samples[0] = context
        while not self.env.done:
            self.self_play_step(self.env, context, target_reward, deterministic=False)
            samples[self.env.episode_steps] = context
        samples = samples[: self.env.episode_steps]

        # fix contexts with actual reward-to-gos
        for i in range(self.env.horizon):
            samples[i]["reward_to_gos"][-i - 1 :] += self.env.episode_reward - target_reward

        self.dataset.max_reward = max(self.dataset.max_reward, self.env.episode_reward)
        self.dataset.min_reward = min(self.dataset.min_reward, self.env.episode_reward)

        self.dataset.replay_buffer.extend(samples)  # replaces oldest elements in replay buffer with new samples
        self.log("self_play_reward", self.env.episode_reward, prog_bar=True)  # type: ignore[arg-type]

    def evaluate(self, *, rendering: bool = False) -> None:
        for target_rew in self.cfg.targets:
            context = self.init_episode(self.val_env, target_rew)
            while not self.val_env.done:
                self.self_play_step(self.val_env, context, target_rew, deterministic=True)  # type: ignore[arg-type]
            if rendering:
                self.make_render()
            self.log(f"{target_rew}_return", self.val_env.episode_reward, prog_bar=True)  # type: ignore[arg-type]
        self.log("val_reward", self.val_env.episode_reward, prog_bar=True)  # type: ignore[arg-type]

    def on_train_epoch_end(self) -> None:
        self.self_play_episode()
        super().on_train_epoch_end()

    def configure_optimizers(self) -> Any:
        self.actor_optimizer = torch.optim.AdamW(
            self.parameters(),
            lr=self.cfg.learning_rate,
            weight_decay=self.cfg.weight_decay,
        )
        self.temperature_optimizer = torch.optim.Adam(
            [self.log_temperature],
            lr=1e-4,
            betas=[0.9, 0.999],  # type:ignore[arg-type]
        )
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(
            self.actor_optimizer,
            lambda steps: min((steps + 1) / self.cfg.lr_warmup_steps, 1),
        )
        return [self.actor_optimizer, self.temperature_optimizer], [{"scheduler": self.scheduler, "interval": "step"}]

    def on_train_batch_end(self, outputs: STEP_OUTPUT, batch: Any, batch_idx: int) -> None:
        self.scheduler.step()  # Why lightning not handling this?
        super().on_train_batch_end(outputs, batch, batch_idx)


if __name__ == "__main__":
    from pathlib import Path

    from iot_rl_model.common.train import train

    train(config_file=Path(__file__).parent.joinpath("odt.yaml"))
