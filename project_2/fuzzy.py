import gym
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Tworzymy środowisko gry w Blackjacka
env = gym.make('Blackjack-v1', natural=True, sab=False)

# Definiujemy zmienne lingwistyczne
# player_sum - suma kart gracza
# dealer_card - wartość karty krupiera
# action - akcja gracza (czy ma dobrać kartę czy nie)
player_sum = ctrl.Antecedent(np.arange(0, 32, 1), 'player_sum')
dealer_card = ctrl.Antecedent(np.arange(0, 11, 1), 'dealer_card')
action = ctrl.Consequent(np.arange(0, 2, 1), 'action')

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
player_sum_input = 12
dealer_card_input = 10

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
#
# # Play the game
# observation = env.reset()
# done = False
# while not done:
#     player_sum, dealer_card, usable_ace = observation
#     action = get_action(player_sum, dealer_card)
#     action = 0 if action < 0.5 else 1  # Convert to 0 or 1
#     observation, reward, done, info = env.step(action)
#     if done:
#         print("Game finished. Reward: ", reward)
#         observation = env.reset()
#
# env.close()

import matplotlib.pyplot as plt

# Initialize a dictionary to store the results
results = {}

# Play 100 games
for _ in range(100):
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


env.close()

# Plot the results
# plt.bar(results.keys(), results.values(), tick_label=['Loss', 'Draw', 'Win'])
plt.bar(results.keys(), results.values())
plt.xlabel('Game Result')
plt.ylabel('Number of Games')
plt.title('Blackjack Game Results')
plt.show()