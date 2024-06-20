import time
import gym
from matplotlib import pyplot as plt

env = gym.make("Blackjack-v1", natural=True, sab=False)

observation, _ = env.reset()

# info about the game
games_to_play = 100
play = True
results = {}

while play:
    print("Player's sum: ", observation)
    player_sum, dealer_card, usable_ace = observation

    action = 1 if player_sum < 17 else 0

    print(env.step(action))
    observation, reward, done, info, _ = env.step(action)

    if done:
        print("The game has been finished.", reward)
        print("Final observation: ", observation)
        # time.sleep(1)
        observation, _ = env.reset()
        if (reward > 1):
            play = False

        # adding our results to the dictionary
        if reward in results:
            results[reward] += 1
        else:
            results[reward] = 1

        # We have to check if we played enough games already, then stop
        if sum(results.values()) >= games_to_play:
            play = False

env.close()

# Plot the results
plt.bar(results.keys(), results.values())
plt.xlabel('Game Result')
plt.ylabel('Number of Games')
plt.title('Blackjack Game Results')
plt.show()