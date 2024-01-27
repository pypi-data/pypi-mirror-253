# import random
# import warnings
# from typing import TYPE_CHECKING, Any, Generator
# from litrl.algo.typing import LitRLModule
# import gymnasium as gym
# import lightning as L
# import numpy as np
# import numpy.typing as npt
# import torch
# from gymnasium.spaces import Box, Discrete
# from tensordict import tensorclass
# from torch.utils.data import DataLoader, Dataset
# from torchmetrics import MeanSquaredError
# from torchrl.data import LazyTensorStorage, TensorDictReplayBuffer
# from torchrl.data.replay_buffers.replay_buffers import TensorDictReplayBuffer
# from tqdm.auto import tqdm

# if TYPE_CHECKING:
#     from litrl.algo.rainbow.config_schema import ModelConfigSchema

# ObsType = npt.NDArray[np.float64]
# Mask = npt.NDArray[np.int8] | None
# ProcessedObsType = torch.Tensor
# ActionType = np.int64


# class DummyDataset(Dataset[None]):
#     def __getitem__(self, index: int) -> Generator[None, None, None]:
#         yield None

#     def __len__(self) -> int:
#         return 1


# @tensorclass
# class Experience:
#     obs: torch.Tensor
#     mask: torch.Tensor | None
#     action: torch.Tensor
#     next_obs: torch.Tensor
#     reward: torch.Tensor
#     terminated: torch.Tensor
#     truncated: torch.Tensor


# class DQN(LitRLModule):
#     def __init__(self, cfg: "ModelConfigSchema[gym.Env]") -> None:
#         super().__init__()
#         self.cfg = cfg
#         self.save_hyperparameters()
#         self.obs, self.mask = self.reset_seed(self.cfg.env, self.cfg.seed)
#         self.build_network()
#         self.buffer = TensorDictReplayBuffer(
#             storage=LazyTensorStorage(max_size=self.cfg.buffer.max_size),
#             batch_size=self.cfg.buffer.batch_size,
#         )
#         self.env = cfg.env
#         self.episode_reward: torch.Tensor = torch.tensor(0.0, dtype=torch.float32)
#         self.criterion = MeanSquaredError()
#         self.net: torch.nn.Module

#     def build_network(self) -> None:
#         obs_features = 1
#         n_actions, observation_shape = self.get_shapes()
#         for dim in observation_shape:
#             obs_features *= dim

#         layers: list[torch.nn.Module] = [torch.nn.Linear(obs_features, self.cfg.hidden_size)]
#         for _ in range(self.cfg.n_hidden_layers):
#             layers.append(torch.nn.Linear(self.cfg.hidden_size, self.cfg.hidden_size))
#             layers.append(torch.nn.ReLU())
#         layers.append(torch.nn.Linear(self.cfg.hidden_size, n_actions))
#         layers.append(torch.nn.Tanh())
#         self.net = torch.nn.Sequential(*layers)

#     def experience_step(self, action: ActionType) -> tuple[float, bool]:
#         next_obs, reward, terminated, truncated, mask = self.env_step(
#             self.cfg.env, action
#         )
#         experience = Experience(
#             obs=self.obs,
#             mask=torch.tensor(self.mask).unsqueeze(0)
#             if self.mask is not None
#             else None,
#             action=torch.tensor(action, dtype=torch.int64).unsqueeze(0),
#             next_obs=next_obs,
#             reward=torch.tensor(reward, dtype=torch.float32).unsqueeze(0),
#             terminated=torch.tensor(terminated, dtype=torch.int8).unsqueeze(0),
#             truncated=torch.tensor(truncated, dtype=torch.int8).unsqueeze(0),
#             batch_size=(1,),
#         )
#         self.buffer.extend(experience.to_tensordict())  # pylint: disable=no-member
#         if terminated or truncated:
#             next_obs, mask = self.reset(self.cfg.env)
#         self.obs = next_obs
#         self.mask = mask
#         return reward, terminated or truncated

#     def env_step(
#         self, env: gym.Env, action: ActionType
#     ) -> tuple[ProcessedObsType, float, bool, bool, Mask]:
#         obs, reward, terminated, truncated, _ = env.step(action)
#         return self.process_obs(obs), reward, terminated, truncated, None

#     def get_shapes(self) -> tuple[int, tuple[int, ...]]:
#         if not isinstance(self.cfg.env.action_space, Discrete):
#             raise ValueError("env action_space is not Discrete")
#         if not isinstance(self.cfg.env.observation_space, Box):
#             raise ValueError("env observation space is not a Box")
#         action_shape = self.cfg.env.action_space.n
#         observation_shape = self.cfg.env.observation_space.shape
#         return action_shape, observation_shape

#     def get_action(
#         self, obs: ProcessedObsType, mask: Mask, random_p: float = 0
#     ) -> np.int64:
#         if random.random() < random_p:
#             return self.random_action()
#         return self.forward(obs, mask)

#     def acquire_experience(self) -> None:
#         reward, done = self.experience_step(
#             self.get_action(self.obs, self.mask, random_p=self.cfg.epsilon)
#         )
#         self.episode_reward += reward
#         if done:
#             self.log("episode_reward", self.episode_reward, prog_bar=True)
#             self.episode_reward = torch.tensor(0.0, dtype=torch.float32)

#     def training_step(self, batch, _):  # type: ignore[no-untyped-def]
#         self.acquire_experience()

#         with torch.no_grad():
#             next_q_values = self.net(batch["next_obs"])
#             next_values = torch.max(next_q_values, dim=-1).values
#         td_target = (1 - batch["terminated"]) * next_values
#         current_q_values = self.net(batch["obs"])
#         current_values = current_q_values.gather(
#             1, batch["action"].unsqueeze(1)
#         ).squeeze(1)
#         pred = current_values + self.cfg.gamma * batch["reward"]
#         loss = self.criterion(pred, td_target)
#         self.log("loss", loss, prog_bar=True)
#         return {"loss": loss}

#     def configure_optimizers(self):  # type: ignore[no-untyped-def]
#         return torch.optim.Adam(self.net.parameters(), lr=self.cfg.lr)

#     def on_train_epoch_end(self) -> None:
#         self.log("buffer_size", torch.tensor(float(len(self.buffer))))
#         return super().on_train_epoch_end()

#     def reset_seed(self, env: gym.Env, seed: int) -> tuple[ProcessedObsType, Mask]:
#         env.reset(seed=seed)
#         return self.reset(env)

#     def reset(self, env: gym.Env) -> tuple[ProcessedObsType, Mask]:
#         obs, _ = env.reset()
#         return self.process_obs(obs), None

#     @torch.no_grad()
#     def validation_step(self, batch: Any) -> None:
#         del batch
#         obs, mask = self.reset_seed(self.cfg.val_env, self.cfg.val_env_seed)
#         terminated, truncated = False, False
#         episode_reward = 0.0
#         while not terminated or truncated:
#             action = self.get_action(obs, mask)
#             obs, reward, terminated, truncated, mask = self.env_step(
#                 self.cfg.val_env, action
#             )
#             self.val_render()
#             episode_reward += float(reward)
#         self.log(
#             "val_reward", torch.tensor(episode_reward), prog_bar=True, batch_size=1
#         )

#     def val_render(self) -> None:
#         match self.cfg.val_env.render_mode:
#             case "human":
#                 self.cfg.val_env.render()
#             case "rgb_array":
#                 raise NotImplementedError
#             case None:
#                 pass
#             case _:
#                 raise NotImplementedError(self.cfg.val_env.render_mode)

#     def forward(self, obs: ProcessedObsType, mask: Mask) -> ActionType:
#         del mask
#         qs = self.net(obs)
#         return qs.argmax().item()  # type: ignore[no-any-return]

#     def random_action(self) -> ActionType:
#         return self.cfg.env.action_space.sample()  # type: ignore[no-any-return]

#     def train_dataloader(self)->DataLoader:
#         for _ in tqdm(range(self.cfg.warm_start_steps)):
#             action = self.random_action()
#             self.experience_step(action)
#         return self.buffer # type: ignore[no-any-return]

#     def val_dataloader(self)->DataLoader[None]:
#         """Return a dummy dataset that will be ignored"""
#         warnings.filterwarnings("ignore", message=".*does not have many workers.*")
#         return DataLoader(DummyDataset(), collate_fn=lambda x: x)

#     @staticmethod
#     def process_obs(obs: ObsType) -> ProcessedObsType:
#         return torch.tensor(obs).unsqueeze(0)  # type: ignore[no-any-return]
