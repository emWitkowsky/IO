import numpy as np
import gym

def value_iteration(env, gamma=0.99, max_iterations=10000, delta=1e-3):
    num_states = env.observation_space.n
    num_actions = env.action_space.n
    V = np.zeros(num_states)

    for i in range(max_iterations):
        prev_V = np.copy(V)

        for state in range(num_states):
            q_sa = [sum([p * (r + gamma * prev_V[s_]) for p, s_, r, _ in env.P[state][action]]) for action in range(num_actions)]
            V[state] = max(q_sa)

        if np.sum(np.fabs(prev_V - V)) <= delta:
            print(f'Value-iteration converged at iteration #{i}.')
            break

    policy = np.zeros(num_states)
    for state in range(num_states):
        q_sa = np.zeros(env.action_space.n)
        for action in range(num_actions):
            q_sa[action] = sum([p * (r + gamma * V[s_]) for p, s_, r, _ in env.P[state][action]])
        policy[state] = np.argmax(q_sa)

    return V, policy

env = gym.make('FrozenLake8x8-v1', is_slippery=False)
optimal_v, optimal_policy = value_iteration(env.env)
print('Optimal Value function: ')
print(optimal_v.reshape((8, 8)))
print('Final Policy: ')
print(optimal_policy.reshape((8, 8)))