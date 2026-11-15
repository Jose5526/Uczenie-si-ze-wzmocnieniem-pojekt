
from dataclasses import dataclass


@dataclass
class RewardConfig:
    "Parameters used to calculate the agent's reward."

    progress_weight: float = 1.0
    collision_penalty: float = 10.0
    off_track_penalty: float = 5.0
    time_penalty: float = 0.01
    finish_reward: float = 100.0


@dataclass
class RewardInput:
    "Information required to calculate a single-step reward."

    progress_delta: float = 0.0
    collision: bool = False
    off_track: bool = False
    elapsed_time: float = 0.0
    finished: bool = False


def calculate_reward(
    data: RewardInput,
    config: RewardConfig = RewardConfig()
) -> float:
    " Calculate the reward received by the agent after one action."

    reward = data.progress_delta * config.progress_weight

    if data.collision:
        reward -= config.collision_penalty

    if data.off_track:
        reward -= config.off_track_penalty

    reward -= data.elapsed_time * config.time_penalty

    if data.finished:
        reward += config.finish_reward

    return reward


if __name__ == "__main__":
    example = RewardInput(
        progress_delta=2.0,
        collision=False,
        off_track=False,
        elapsed_time=0.1,
        finished=False
    )

    print("Calculated reward:", calculate_reward(example))
