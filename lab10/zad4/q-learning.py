import gym
import numpy as np
import matplotlib.pyplot as plt

# We set the environment for our Blackjack game
env = gym.make('Blackjack-v1', natural=False, sab=False)

# Q-learning params
alpha = 0.7  # Learning rate
gamma = 0.4  # Discount factor
epsilon = 0.7  # Exploration rate
num_episodes = 500000

alpha_decay = 0.9999
# gamma_decay = 0.9999
epsilon_decay = 0.9999

# Let's set the Q-table with zeros
q_table = np.zeros((32, 11, 2, 2))  # (player's sum, dealer's card, usable ace, action)

# Function to choose the next action
def choose_action(state):
    player_sum, dealer_card, usable_ace = state
    if np.random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Explore
    else:
        return np.argmax(q_table[player_sum, dealer_card, int(usable_ace)])  # Exploit

# Stats for our game (training season)
wins = 0
losses = 0
# We set the list where we store the rewards and their number of occurrences
total_rewards = []
total_reward_sum = 0

# So it begins... training the agent
for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0  # Reward our agent gets in each episode

    while not done:
        if isinstance(state[0], tuple):  # Check if the first element of state is a tuple
            game_state, _ = state  # Unpack the outer tuple
            player_sum, dealer_card, usable_ace = game_state  # Unpack the inner tuple and write their values
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

        # total_rewards.append(total_reward)
        total_reward_sum += total_reward
        total_rewards.append(total_reward_sum / (episode + 1))
        epsilon *= epsilon_decay
        alpha *= alpha_decay


print(f"Number of wins: {wins}")
print(f"Number of losses: {losses}")

# Test the trained agent
num_test_episodes = 100
test_wins = 0
test_losses = 0

for episode in range(num_test_episodes):
    state = env.reset()
    done = False

    while not done:
        if isinstance(state[0], tuple):  # Check if the first element of state is a tuple
            game_state, _ = state  # Unpack the outer tuple
            player_sum, dealer_card, usable_ace = game_state  # Unpack the inner tuple and write their values
        else:
            player_sum, dealer_card, usable_ace = state  # Unpack the state directly

        # Choose action based on Q-table (no random actions)
        action = np.argmax(q_table[player_sum, dealer_card, int(usable_ace)])
        next_state, reward, done, info, _ = env.step(action)

        state = next_state

        # Update wins and losses counters
        if done:
            if reward == 1:
                test_wins += 1
            elif reward == -1:
                test_losses += 1

print(f"Number of wins in test: {test_wins}")
print(f"Number of losses in test: {test_losses}")

print(f"Win percentage during test: {test_wins / 100 * 100}%")

plt.plot(total_rewards)
plt.xlabel('Episode')
plt.ylabel('Average Reward')
plt.title('Average Reward per Episode')
plt.show()
