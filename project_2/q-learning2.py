import gym
import numpy as np
import matplotlib.pyplot as plt

# Initialize the Blackjack environment
env = gym.make('Blackjack-v1', natural=False, sab=False)

# Q-learning parameters
alpha = 0.7  # Learning rate
gamma = 0.3  # Discount factor
epsilon = 0.8  # Exploration rate
num_episodes = 100

# Initialize the Q-table with zeros
q_table = np.zeros((32, 11, 2, 2))  # (player's sum, dealer's card, usable ace, action)

# Function to choose the next action
def choose_action(state):
    player_sum, dealer_card, usable_ace = state
    if np.random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Explore
    else:
        return np.argmax(q_table[player_sum, dealer_card, int(usable_ace)])  # Exploit

# # Training the agent
# for episode in range(num_episodes):
#     state = env.reset()
#     done = False
#
#     while not done:
#         print(f"Current state: {state}")  # Add this line
#         game_state, _ = state  # Unpack the outer tuple
#         player_sum, dealer_card, usable_ace = game_state  # Unpack the inner tuple
#         # player_sum, dealer_card, usable_ace = state
#         action = choose_action(game_state)
#         next_state, reward, done, truncated, info = env.step(action)
#         next_player_sum, next_dealer_card, next_usable_ace = next_state
#
#         # Update Q-table
#         old_value = q_table[player_sum, dealer_card, int(usable_ace), action]
#         if not done:
#             next_max = np.max(q_table[next_player_sum, next_dealer_card, int(next_usable_ace)])
#         else:
#             next_max = 0  # No future state value if done
#
#         q_table[player_sum, dealer_card, int(usable_ace), action] = \
#             old_value + alpha * (reward + gamma * next_max - old_value)
#
#         state = next_state

wins = 0
losses = 0
# Initialize list to store average rewards
total_rewards = []

# Training the agent
for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0  # Initialize total reward for this episode

    while not done:
        # print(f"Current state: {state}")  # Add this line
        if isinstance(state[0], tuple):  # Check if the first element of state is a tuple
            game_state, _ = state  # Unpack the outer tuple
            player_sum, dealer_card, usable_ace = game_state  # Unpack the inner tuple
        else:
            player_sum, dealer_card, usable_ace = state  # Unpack the state directly
        action = choose_action((player_sum, dealer_card, usable_ace))
        next_state, reward, done, truncated, info = env.step(action)
        if isinstance(next_state[0], tuple):  # Check if the first element of next_state is a tuple
            next_game_state, _ = next_state
            next_player_sum, next_dealer_card, next_usable_ace = next_game_state
        else:
            next_player_sum, next_dealer_card, next_usable_ace = next_state

        total_reward += reward
        # Update Q-table
        old_value = q_table[player_sum, dealer_card, int(usable_ace), action]
        if not done:
            next_max = np.max(q_table[next_player_sum, next_dealer_card, int(next_usable_ace)])
        else:
            next_max = 0  # No future state value if done

        q_table[player_sum, dealer_card, int(usable_ace), action] = \
            old_value + alpha * (reward + gamma * next_max - old_value)

        state = next_state

        # Update wins and losses counters
        if done:
            if reward == 1:
                wins += 1
            elif reward == -1:
                losses += 1

        # At the end of the episode, calculate average reward and add to list
        # average_reward = total_reward / num_episodes
        # average_rewards.append(average_reward)
        total_rewards.append(total_reward)


print(f"Number of wins: {wins}")
print(f"Number of losses: {losses}")

print('Q-table after training:')
# print(q_table)
np.savetxt('q_table.txt', q_table.flatten(), fmt='%f')

print("Average rewards per episode:")
for i, reward in enumerate(total_rewards):
    print(f"Episode {i+1}: {reward}")

plt.plot(total_rewards)
plt.xlabel('Episode')
plt.ylabel('Average Reward')
plt.title('Average Reward per Episode')
plt.show()
