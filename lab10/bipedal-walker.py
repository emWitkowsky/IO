import gym
import Box2D

env = gym.make("BipedalWalker-v3", render_mode="human")
observation, info = env.reset(seed=278779)

for i in range(300):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()