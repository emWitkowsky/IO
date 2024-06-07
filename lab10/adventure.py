import gym

env = gym.make("ALE/Adventure-v5", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(10):
    action = 5
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()

for _ in range(30):
    action = 4
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()

for _ in range(10):
    action = 2
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()

for _ in range(20):
    action = 4
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()

# for _ in range(500):
#     action = env.action_space.sample()
#     observation, reward, terminated, truncated, info = env.step(action)
#     if terminated or truncated:
#         observation, info = env.reset()
env.close()