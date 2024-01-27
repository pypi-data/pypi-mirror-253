import pickle  # nosec
from pathlib import Path
from typing import TYPE_CHECKING, Any

import numpy as np
import torch
from gymnasium.spaces import Box
from loguru import logger
from tensordict import TensorDict  # type:ignore[import]
from tqdm.auto import tqdm

from .context import init_context, update_context

try:
    from torchrl.data import LazyTensorStorage  # type:ignore[import]
    from torchrl.data import TensorDictReplayBuffer
except ImportError as e:
    logger.error(e)

if TYPE_CHECKING:
    from numpy.typing import NDArray

    Sample = tuple[RewardType, ObservationType, NDArray[Any]]
    Trajectory = list[Sample]


class DTDataset:
    def __init__(  # noqa: PLR0913
        self,
        env: BaseEnv,
        n_samples: int,
        context_length: int,
        batch_size: int,
        batches_per_epoch: int,
        *,
        force_generate: bool = False,
    ) -> None:
        self.batches_per_epoch = batches_per_epoch
        self.context_length = context_length
        self.n_samples = n_samples
        self.replay_buffer = TensorDictReplayBuffer(
            storage=LazyTensorStorage(n_samples),
            batch_size=batch_size,
        )
        self.load_data(
            env,
            force_generate=force_generate,
        )

    def sample(self) -> TensorDict:
        return self.replay_buffer.sample()

    def generate_data(
        self,
        env: BaseEnv[Box],
        info_path: Path,
    ) -> None:
        self.min_reward: RewardType = np.float64("inf")
        self.max_reward: RewardType = -np.float64("inf")

        samples = TensorDict(
            {
                "observations": torch.empty((self.n_samples, self.context_length, env.observation_space.shape[0])),
                "actions": torch.empty((self.n_samples, self.context_length, env.action_space.shape[0])),
                "reward_to_gos": torch.empty((self.n_samples, self.context_length, 1)),
                "timesteps": torch.empty((self.n_samples, self.context_length, 1), dtype=torch.int64),
                "mask": torch.empty((self.n_samples, self.context_length, 1), dtype=torch.bool),
            },
            batch_size=(self.n_samples, self.context_length),
        )
        trajectory: "Trajectory" = []
        for i in tqdm(range(self.n_samples), desc="Generating offline dataset"):
            if len(trajectory) == 0:
                obs, _ = env.reset()
                while not env.done:
                    action = env.action_space.sample()
                    next_obs, reward, _, _, _ = env.step(action)
                    trajectory.append((reward, obs, action))
                    obs = next_obs
                self.min_reward = min(self.min_reward, env.episode_reward)
                self.max_reward = max(self.max_reward, env.episode_reward)
                context = init_context(
                    self.context_length,
                    env.observation_space.shape[0],
                    env.action_space.shape[0],
                )
                reward_to_go = env.episode_reward

            reward, obs, action = trajectory.pop(0)
            update_context(
                context,
                reward_to_go,
                torch.from_numpy(obs).float(),
                torch.from_numpy(action).float(),
            )
            reward_to_go -= reward
            samples[i] = context

        observations = samples["observations"].reshape(-1, env.observation_space.shape[0])
        mask = samples["mask"].flatten()
        self.observation_mean = observations[mask].mean(dim=0)
        self.observation_std = observations[mask].std(dim=0)
        samples["observations"] -= self.observation_mean
        samples["observations"] /= self.observation_std + 1e-6

        with info_path.open("wb") as f:
            logger.info(f"Saving data to {info_path}")
            pickle.dump(
                {
                    "samples": samples,
                    "observation_mean": self.observation_mean,
                    "observation_std": self.observation_std,
                    "min_reward": self.min_reward,
                    "max_reward": self.max_reward,
                },
                f,
            )
        self.replay_buffer.extend(samples)

    def load_data(
        self,
        env: BaseEnv[Box],
        *,
        force_generate: bool,
    ) -> None:
        data_path = Path().joinpath("results", "data")
        data_path.mkdir(exist_ok=True, parents=True)
        info_path = data_path.joinpath(f"{env!r}|{self.n_samples:.1E}.pickle")
        if not info_path.exists() or force_generate:
            self.generate_data(env, info_path)
        else:
            logger.info(f"Loading data from {info_path}")
            with info_path.open("rb") as f:
                info = pickle.load(f)  # nosec

            logger.info("Data successfully loaded")
            samples = info["samples"]
            self.observation_mean = info["observation_mean"]
            self.observation_std = info["observation_std"]
            self.min_reward = info["min_reward"]
            self.max_reward = info["max_reward"]
            self.replay_buffer.extend(samples)
