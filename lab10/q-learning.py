import gym
import numpy as np

# Initialize the Blackjack environment
env = gym.make('Blackjack-v1', natural=False, sab=False)

# Q-learning parameters
alpha = 0.5  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
num_episodes = 50000

# Initialize the Q-table with zeros
q_table = np.zeros((32, 11, 2))  # (player's sum, dealer's card, usable ace)

# Function to choose the next action
def choose_action(state):
    player_sum, dealer_card, _ = state[0]  # if state is a nested tuple
    player_sum = int(player_sum)
    dealer_card = int(dealer_card)
    if np.random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Explore
    else:
        return np.argmax(q_table[player_sum, dealer_card])  # Exploit

# Training the agent
for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        player_sum, dealer_card, usable_ace = state
        player_sum = int(player_sum)
        dealer_card = int(dealer_card)
        action = choose_action(state)
        action = int(action)
        next_state, reward, done, truncated, info = env.step(action)
        next_player_sum, next_dealer_card, next_usable_ace = next_state

        # Update Q-table
        q_table[player_sum, dealer_card, action] = \
            q_table[player_sum, dealer_card, action] + \
            alpha * (reward + gamma * np.max(q_table[next_player_sum, next_dealer_card]) -
                     q_table[player_sum, dealer_card, action])

        state = next_state

print('Q-table after training:')
print(q_table)