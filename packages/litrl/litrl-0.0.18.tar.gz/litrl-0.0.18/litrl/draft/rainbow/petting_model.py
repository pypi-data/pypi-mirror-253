# from typing import TYPE_CHECKING

# import numpy as np
# import numpy.typing as npt
# import torch
# from loguru import logger
# from pettingzoo import AECEnv

# from litrl.algo.rainbow.model import DQN

# if TYPE_CHECKING:
#     from litrl.algo.rainbow.config_schema import ModelConfigSchema

# ObsType = dict
# ActionType = np.int64
# ProcessedObsType = torch.Tensor
# Mask = npt.NDArray[np.int8]


# class WrongPlayerError(Exception):
#     pass


# class PettingDQN(DQN):
#     """Train DQN in a pettingzoo env.

#     The opponent is always 'player_0' and is a random agent.  # TODO extend
#     """

#     def __init__(self, cfg: "ModelConfigSchema[AECEnv]") -> None:
#         super().__init__(cfg)
#         self.cfg: "ModelConfigSchema[AECEnv]"

#     def random_action(self) -> np.int64:
#         if self.cfg.env.agent_selection != "player_1":
#             raise WrongPlayerError()
#         return self.cfg.env.action_space("player_1").sample(self.mask)

#     def opponent_action(self, env: AECEnv, obs=None) -> None:
#         if env.agent_selection != "player_0":
#             raise WrongPlayerError()
#         obs = obs or env.observe("player_0")
#         return env.action_space("player_0").sample(obs["action_mask"])

#     def env_step(
#         self, env: AECEnv, action
#     ) -> tuple[ProcessedObsType, float, bool, bool, Mask]:
#         if env.agent_selection != "player_1":
#             raise WrongPlayerError()
#         env.step(action)  # check if reward should be reward from both players
#         (
#             obs,
#             opponent_reward,
#             terminated,
#             truncated,
#             _,
#         ) = env.last()  # info from opponent's perspective
#         if not terminated and not truncated:
#             if env.agent_selection != "player_0":
#                 raise WrongPlayerError()
#             opponent_action = self.opponent_action(env, obs)
#             env.step(opponent_action)
#             if env.agent_selection != "player_1":
#                 raise WrongPlayerError()
#             (
#                 obs,
#                 player_reward,
#                 terminated,
#                 truncated,
#                 _,
#             ) = env.last()  # info from our perspective
#             reward = player_reward
#         else:
#             reward = -opponent_reward  # Bad reward for opponent is good for us
#         return self.process_obs(obs), reward, terminated, truncated, obs["action_mask"]

#     def reset_seed(self, env: AECEnv, seed: int) -> tuple[ProcessedObsType, Mask]:
#         env.reset(seed=seed)
#         return self.reset(env)

#     def reset(self, env: AECEnv) -> tuple[ProcessedObsType, Mask]:
#         env.reset()
#         if env.agent_selection != "player_0":
#             raise WrongPlayerError()
#         opponent_action = self.opponent_action(env)
#         env.step(opponent_action)
#         if env.agent_selection != "player_1":
#             raise WrongPlayerError()
#         obs = env.observe("player_1")
#         return self.process_obs(obs), obs["action_mask"]

#     def forward(self, obs: ProcessedObsType, mask: Mask) -> ActionType:
#         qs: torch.Tensor = self.net(obs)
#         qs = qs.masked_fill(torch.tensor(mask == 0), -np.inf)
#         return qs.argmax().item()

#     @staticmethod
#     def process_obs(obs: ObsType) -> torch.Tensor:
#         return (
#             torch.tensor(obs["observation"], dtype=torch.float32).flatten().unsqueeze(0)
#         )

#     def get_shapes(self) -> tuple[int, tuple[int, ...]]:
#         return (
#             int(self.cfg.env.action_space(self.cfg.env.agent_selection).n),
#             self.cfg.env.observation_space(self.cfg.env.agent_selection)[
#                 "observation"
#             ].shape,
#         )
