import gym
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# We create the environment for the game
# natural = True means that the game will be played with the natural blackjack rules
# sab = False means that the game will be played with a single deck
env = gym.make('Blackjack-v1', natural=True, sab=False)

# Parameters of game
games_to_play = 100

# We define the input and output variables
# player_sum - player's hand value
# dealer_card - value of the dealer's face-up card
# action - player's action (stick or hit)
player_sum = ctrl.Antecedent(np.arange(0, 32, 1), 'player_sum')
dealer_card = ctrl.Antecedent(np.arange(0, 11, 1), 'dealer_card')
action = ctrl.Consequent(np.arange(0, 2, 1), 'action')

usable_ace = ctrl.Antecedent(np.arange(2), 'usable_ace')
usable_ace['no'] = fuzz.trimf(usable_ace.universe, [0, 0, 0])
usable_ace['yes'] = fuzz.trimf(usable_ace.universe, [1, 1, 1])

# We define the membership functions for each variable
# setting the sets for every point so that the fuzzy system can work on them
player_sum['low'] = fuzz.trimf(player_sum.universe, [0, 0, 15])
player_sum['medium'] = fuzz.trimf(player_sum.universe, [10, 15, 20])
player_sum['high'] = fuzz.trimf(player_sum.universe, [15, 30, 30])

dealer_card['low'] = fuzz.trimf(dealer_card.universe, [0, 0, 5])
dealer_card['medium'] = fuzz.trimf(dealer_card.universe, [2, 5, 8])
dealer_card['high'] = fuzz.trimf(dealer_card.universe, [5, 10, 10])

action['stick'] = fuzz.trimf(action.universe, [0, 0, 0.5])
action['hit'] = fuzz.trimf(action.universe, [0.5, 1, 1])

# We define set of rules that will determine the action
rule1 = ctrl.Rule(player_sum['low'], action['hit'])
rule2 = ctrl.Rule(player_sum['medium'] & dealer_card['low'], action['stick'])
rule3 = ctrl.Rule(player_sum['medium'] & dealer_card['medium'], action['hit'])
rule4 = ctrl.Rule(player_sum['medium'] & dealer_card['high'], action['hit'])
rule5 = ctrl.Rule(player_sum['high'], action['stick'])

# Control system and simulation
action_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
action_sim = ctrl.ControlSystemSimulation(action_ctrl)

# Simulate the fuzzy system
player_sum_input = 17
dealer_card_input = 4

action_sim.input['player_sum'] = player_sum_input
action_sim.input['dealer_card'] = dealer_card_input

# Compute the action
action_sim.compute()

print(action_sim.output['action'])

def get_action(player_sum_input, dealer_card_input):
    action_sim.input['player_sum'] = player_sum_input
    action_sim.input['dealer_card'] = dealer_card_input
    action_sim.compute()
    return action_sim.output['action']

# Initialize a dictionary to store the results
results = {}
wins = 0
losses = 0

# Play 100 games
for _ in range(games_to_play):
    observation, _ = env.reset()
    done = False
    while not done:
        player_sum, dealer_card, usable_ace = observation
        action = get_action(player_sum, dealer_card)
        action = 0 if action < 0.5 else 1  # Convert to 0 or 1
        observation, reward, done, info, _ = env.step(action)
        if done:
            # Update the results dictionary
            if reward in results:
                results[reward] += 1
            else:
                results[reward] = 1
            observation, _ = env.reset()

        if (reward >= 1):
            wins += 1
        else:
            losses += 1
        break

env.close()

print("Wins: ", wins)
print("Losses: ", losses)
print(f"Win percentage: ", wins / games_to_play * 100, "%" )


# Plot the results
plt.bar(results.keys(), results.values())
plt.xlabel('Game Result')
plt.ylabel('Number of Games')
plt.title('Blackjack Game Results')
plt.show()