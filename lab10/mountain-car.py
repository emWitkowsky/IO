import gym

env = gym.make('MountainCar-v0', render_mode="human")
observation, info = env.reset(seed=42)

for i in range(10):
    for _ in range(2*i):
        action = 2
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()
    for _ in range(5*i):
        action = 0
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()
    for _ in range(2*i):
        action = 1
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()


env.close()