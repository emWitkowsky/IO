import gym
import numpy as np

def discretize_state(env, state):
    # Define the bounds for each state dimension
    bounds = list(zip(env.observation_space.low, env.observation_space.high))
    bounds[1] = [-0.07, 0.07]  # Limit velocity bounds for stability

    # Define the number of bins for each state dimension
    num_bins = (10, 10)

    # Discretize each state dimension
    discretized_state = []
    for i in range(len(state)):
        scaling = (state[i] - bounds[i][0]) / (bounds[i][1] - bounds[i][0])
        new_state = int(np.round((num_bins[i] - 1) * scaling))
        new_state = min(num_bins[i] - 1, max(0, new_state))
        discretized_state.append(new_state)

    return tuple(discretized_state)

def q_learning(env, alpha=0.5, gamma=0.95, epsilon=0.1, num_episodes=50000):
    num_states = (10, 10)  # Update to match discretized state space
    num_actions = env.action_space.n

    # Initialize Q table
    Q = np.zeros(num_states + (num_actions,))

    for episode in range(num_episodes):
        state = discretize_state(env, env.reset())
        done = False

        while not done:
            # Choose action using epsilon-greedy strategy
            if np.random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()  # Explore action space
            else:
                action = np.argmax(Q[state])  # Exploit learned values

            next_state, reward, done, _ = env.step(action)
            next_state = discretize_state(env, next_state)

            # Update Q-table using the Q-learning update rule
            Q[state][action] = (1 - alpha) * Q[state][action] + alpha * (reward + gamma * np.max(Q[next_state]))

            state = next_state

        if episode % 1000 == 0:
            print(f'Episode: {episode}')

    # Derive policy from Q-table
    policy = np.argmax(Q, axis=2)

    return Q, policy

env = gym.make('MountainCar-v0')
Q, policy = q_learning(env)
print('Q-table:')
print(Q)
print('Policy:')
print(policy)
env.close()