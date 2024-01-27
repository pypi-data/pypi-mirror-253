import torch
from tensordict import TensorDict  # type: ignore[import]


def init_context(
    context_length: int,
    state_dim: int,
    action_dim: int,
) -> TensorDict:
    return TensorDict(
        {
            "observations": torch.zeros((context_length, state_dim), dtype=torch.float32),
            "actions": torch.zeros((context_length, action_dim), dtype=torch.float32),
            "reward_to_gos": torch.zeros((context_length, 1), dtype=torch.float32),
            "timesteps": torch.zeros((context_length, 1), dtype=torch.int64),
            "mask": torch.zeros((context_length, 1), dtype=torch.bool),
        },
        batch_size=(context_length,),
    )


def update_context(
    context: TensorDict,
    reward_to_go: torch.Tensor,
    obs: torch.Tensor,
    action: torch.Tensor,
) -> None:
    # shift context by one step
    context[:-1] = torch.clone(context[1:])
    context["observations"][-1] = obs
    context["actions"][-1] = action
    context["reward_to_gos"][-1] = reward_to_go
    context["timesteps"][-1] += 1
    context["mask"][-1] = True
