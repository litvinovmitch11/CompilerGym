# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""Fuzz test LLVM backend using llvm-stress."""
from compiler_gym.envs import LlvmEnv
from tests.pytest_plugins.random_util import apply_random_trajectory
from tests.test_main import main

pytest_plugins = ["tests.pytest_plugins.llvm"]

# The uniform range for trajectory lengths.
RANDOM_TRAJECTORY_LENGTH_RANGE = (1, 10)


def test_fuzz(env: LlvmEnv, observation_space: str, reward_space: str):
    """This test produces a random trajectory using a program generated using
    llvm-stress.
    """
    env.benchmark = env.datasets["llvm-stress-v0"].random_benchmark()

    env.observation_space = observation_space
    env.reward_space = reward_space

    env.reset()
    apply_random_trajectory(
        env,
        random_trajectory_length_range=RANDOM_TRAJECTORY_LENGTH_RANGE,
        timeout=10,
    )
    print(env.state)  # For debugging in case of failure.


if __name__ == "__main__":
    main()
