import gym
import numpy as np

env = gym.make('FrozenLake8x8-v1', render_mode="human", is_slippery=False)


observation, info = env.reset(seed=42)

for _ in range(7):
    action = 2
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()

for _ in range(7):
    action = 1
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()

env.close()