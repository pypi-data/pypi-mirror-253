import math
from typing import Any, Iterable

import einops
import torch
from iot_rl_env.project_typing import ObservationType
from iot_rl_model.common.base_module import BaseModule
from iot_rl_model.common.rescale import rescale_tan
from tensordict import TensorDict  # type: ignore[import]
from torch import nn  # type: ignore[import]
from transformers.modeling_utils import Conv1D  # type:ignore[import]

from .config_class import DTContinuousConfig
from .context import init_context, update_context
from .dataset import DTDataset

MODALITIES = 3  # reward_to_go, observation, action
MASK_BIAS = -1e4  # values to overwrite masked values with


class Block(nn.Module):  # type: ignore[misc]
    def __init__(self, embed_dim: int, n_head: int, dropout: float, context_length: int) -> None:
        super().__init__()
        self.layer_norm = nn.LayerNorm(embed_dim)
        self.n_head = n_head
        self.embed_dim = embed_dim
        # Decoder can't condition on future tokens -> lookahead masking
        self.future_tokens = torch.triu(
            torch.ones(context_length * MODALITIES, context_length * MODALITIES),
            diagonal=1,
        ).bool()
        # Conv1D basically works like a linear layer but the weights are transposed. Radford et al. 2018
        self.c_attention = Conv1D(MODALITIES * self.embed_dim, self.embed_dim)
        self.c_projection = Conv1D(self.embed_dim, self.embed_dim)
        self.dropout = nn.Dropout(dropout)
        self.mlp = nn.Sequential(
            nn.LayerNorm(self.embed_dim),
            Conv1D(4 * self.embed_dim, self.embed_dim),
            nn.ReLU(),
            Conv1D(self.embed_dim, 4 * self.embed_dim),
            nn.Dropout(dropout),
        )

    def forward(
        self,
        hidden_states: torch.Tensor,
        mask: torch.Tensor,
    ) -> torch.Tensor:
        cross_attention = self.c_attention(self.layer_norm(hidden_states))
        # separate the hidden states into key, query and value representations
        query, key, value = cross_attention.split(self.embed_dim, dim=2)

        # split the attention heads, does nothing if using a single head
        query = einops.rearrange(query, "b (m c) (h e) -> b h (m c) e", m=MODALITIES, h=self.n_head)
        key = einops.rearrange(key, "b (m c) (h e) -> b h e (m c)", m=MODALITIES, h=self.n_head)
        value = einops.rearrange(value, "b (m c) (h e) -> b h (m c) e", m=MODALITIES, h=self.n_head)

        # calculate the attention matrix
        attention = torch.matmul(query, key)
        # scale for training stablility (variance = 1)
        attention /= math.sqrt(self.embed_dim / self.n_head)

        # set attention to future tokens to -inf (-> 0 after softmax)
        attention[:, :, self.future_tokens] = MASK_BIAS
        # set attention to padded tokens to -inf (-> 0 after softmax)
        attention += ~mask * MASK_BIAS
        attention = torch.nn.functional.softmax(attention, dim=-1)
        attention = self.dropout(attention)

        score = torch.matmul(attention, value)
        # merge attention heads, does nothing if n_head = 0
        score = einops.rearrange(score, "b h (m c) e->b (m c) (h e)", m=MODALITIES)
        score = self.c_projection(score)
        score = self.dropout(score)
        # residual connection
        hidden_states = score + hidden_states
        # 2nd residual connection
        return hidden_states + self.mlp(hidden_states)


class DTContinuous(BaseModule[DTContinuousConfig]):
    """Concise implementation of Offline Decision Transformers.

    Here, the einops keys for tensor manipulation refer to:
    b: batch size
    m: number of modalities (3 in our case: observations, rewards, actions)
    c: context length (number of steps in the context)
    e: embedding dimension
    h: number of heads in the multi-head attention
    """

    def __init__(self, cfg: DTContinuousConfig) -> None:
        super().__init__(cfg)
        # load a dataset of transitions from the environment
        # if dataset doesn't exist, use random policy to collect n_samples transitions
        self.dataset = DTDataset(
            self.env,
            self.cfg.n_samples,
            self.cfg.context_length,
            self.cfg.batch_size,
            self.cfg.batches_per_epoch,
        )

    def build_networks(self) -> None:
        self.layer_norm = nn.LayerNorm(self.cfg.embed_dim)
        self.dropout = nn.Dropout(self.cfg.dropout)
        self.blocks: Iterable[Block] = nn.ModuleList(
            [
                Block(self.cfg.embed_dim, self.cfg.n_head, self.cfg.dropout, self.cfg.context_length)
                for _ in range(self.cfg.n_layer)
            ],
        )
        self.apply(self._init_weights)  # paper only initializes the transformer layers
        # map each timestep in [0, horizon] to a hidden representation of size self.cfg.embed_dim
        self.embed_position = nn.Embedding(self.env.max_episode_steps, self.cfg.embed_dim)

        self.embed_return = torch.nn.Linear(1, self.cfg.embed_dim)
        self.embed_observation = torch.nn.Linear(self.cfg.state_dim, self.cfg.embed_dim)
        self.embed_action = torch.nn.Linear(self.cfg.action_dim, self.cfg.embed_dim)
        self.layer_norm = nn.LayerNorm(self.cfg.embed_dim)
        self.predict_action = nn.Sequential(nn.Linear(self.cfg.embed_dim, self.cfg.action_dim), nn.Tanh())

    def _init_weights(self, module: nn.Module) -> None:
        if isinstance(module, (nn.Embedding, Conv1D)):
            module.weight.data.normal_(std=0.02)
            if isinstance(module, (Conv1D)) and module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)

    def forward(self, batch: TensorDict) -> torch.Tensor:  # type: ignore[override]
        """Predict the next action given past context.

        batch is the following TensorDict:
            "observations": (batch_size, context_length, obs_dim),
            "actions": (batch_size, context_length, action_dim),
            "reward_to_gos": (batch_size, context_length, 1,
            "timesteps": (batch_size, context_length, 1), dtype=torch.int64,
            "mask": (batch_size, context_length, 1), dtype=torch.bool,

        mask is a boolean that indicates which values have been padded.
        E.g. the first decision point has no context so the values are meaningless.
        We should pay 0 attention to these values
        """
        position_embeddings = self.embed_position(batch["timesteps"].squeeze(-1))

        # embed each modality with a different head and add position embeddings
        observation_embeddings = self.embed_observation(batch["observations"]) + position_embeddings
        action_embeddings = self.embed_action(batch["actions"]) + position_embeddings
        returns_embeddings = self.embed_return(batch["reward_to_gos"]) + position_embeddings

        # [[rtg0...rtgn], [s0...sn], [a0...an]] -> (rtg0, s0, a0, rtg1, s1, a1, ...)
        inputs = einops.rearrange(
            [returns_embeddings, observation_embeddings, action_embeddings],
            "m b c e -> b (c m) e",
        )
        inputs = self.layer_norm(inputs)

        # repeat the mask so it matches the stacked inputs
        mask = einops.repeat(batch["mask"], "b c 1 -> b 1 1 (c m)", m=3)
        hidden_states = self.dropout(inputs)
        for block in self.blocks:
            hidden_states = block.forward(
                hidden_states,
                mask=mask,
            )
        hidden_state = self.layer_norm(hidden_states)
        # reshape so we can extract the hidden state of the observation modality
        hidden_state = einops.rearrange(hidden_state, "b (c m) e-> b m c e", m=MODALITIES)

        # [:, 1] selects the hidden state of the observation modality
        action = self.predict_action(hidden_state[:, 1])
        # tanh activation [-1, 1] -> rescale to the action space
        return rescale_tan(action, self.cfg.min_action, self.cfg.max_action)

    def training_step(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        """Perform 1 forward and backward pass through the network.

        Conceptually, we want to do the following:
        1) from action sequence
            (rtg_0, s_0, a_0, ..., rtg_n, s_n, a_n),
        get hidden states (position embeddings + modality embeddings -> transformer output)
            (h_rtg_0, h_s_0, h_a_0, ..., h_rtg_n, h_s_n, h_a_n)
        2) extract the hidden state of the observation modality:
            (h_s_0 ,..., h_s_n)  # h_s_t is agnostic to a_t due to position masking in transformer
        3) predict next tokens:
            f(h_s_0 ,..., h_s_n) -> (ahat_0, ..., ahat_n) ~= a_0, a_1
        4) ignore loss for padded values
        """
        batch = self.dataset.sample()
        action_preds = self.forward(batch)[batch["mask"]]
        action_targets = batch["actions"][batch["mask"]]
        return {"loss": torch.mean((action_preds - action_targets) ** 2)}

    def normalize_observation(self, obs: ObservationType) -> torch.Tensor:  # type: ignore[override]
        return (torch.from_numpy(obs).float() - self.dataset.observation_mean) / (self.dataset.observation_std + 1e-6)

    @torch.no_grad()
    def evaluate(self, *, rendering: bool = False) -> None:
        """Evaluate the current model preformance on the validation environment."""
        for target_rew in self.cfg.targets:
            # Prompt: Create a trajectory where the cumulative reward is target_rew
            obs, _ = self.val_env.reset()
            context = init_context(  # padded context
                self.cfg.context_length,
                self.cfg.state_dim,
                self.cfg.action_dim,
            )
            # context is now: (padded..., target_rew, s0, pad_action)
            update_context(
                context,
                reward_to_go=target_rew,
                obs=self.normalize_observation(obs),
                action=torch.zeros(self.cfg.action_dim, dtype=torch.float32),
            )
            while not self.val_env.done:
                actions = self.forward(context.unsqueeze(0)).squeeze(0)
                action = actions[-1]  # batch_size 1 so select first batch. Extract last action
                # (padded..., target_rew, s0, unknown_action) -> (padded..., target_rew, s0, a0)
                context["actions"][-1] = action
                obs, _, _, _, _ = self.val_env.step(action.numpy())
                # (padded..., target_rew, s0, a0) -> (padded..., target_rew, s0, a0, target_rew-r0, s1, pad_action)
                update_context(
                    context,
                    target_rew - self.val_env.episode_reward,
                    self.normalize_observation(obs),
                    torch.zeros(self.cfg.action_dim, dtype=torch.float32),
                )
            if rendering:
                self.make_render()
            self.log(f"{target_rew}_return", self.val_env.episode_reward, prog_bar=True)  # type:ignore[arg-type]
        self.log("val_reward", self.val_env.episode_reward, prog_bar=True)  # type:ignore[arg-type]

    def configure_optimizers(self) -> Any:
        optimizer = torch.optim.AdamW(
            self.parameters(),
            lr=self.cfg.learning_rate,
            weight_decay=self.cfg.weight_decay,
        )
        scheduler = torch.optim.lr_scheduler.LambdaLR(
            optimizer,
            lambda steps: min((steps + 1) / self.cfg.lr_warmup_steps, 1),
        )
        return [optimizer], [{"scheduler": scheduler, "interval": "step"}]
