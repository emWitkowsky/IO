import gym
import numpy as np
import pygad
from matplotlib import pyplot as plt

# We set the environment for the game of Blackjack
env = gym.make('Blackjack-v1')

# Genetic Algorithm params
num_generations = 500 # Nothing really changes after 500 generations, except the time we waste
# or maybe it does
num_parents_mating = 100

# Let's init the population
num_player_states = 32  # Player sum can be from 0 to 31
num_dealer_states = 10  # Dealer's face-up card can be from 1 to 10
num_ace_states = 2  # Usable ace can be True or False

# The total number of states is the product of the number of states for each observation
num_states = num_player_states * num_dealer_states * num_ace_states

# Init population with random strategies
initial_population = np.random.choice([0, 1], size=(num_parents_mating, num_states))

def fitness_func(ga_instance, solution, solution_idx):
    total_reward = 0
    win_count = 0
    # print("Generation: ", ga_instance.generations_completed, "Solution: ", solution, "Fitness: ", solution_fitness)
    # print(ga_instance.generations_completed, "Solution: ", solution, "Fitness: ", solution_fitness)
    for _ in range(100):  # Evaluate strategy over 100 games
        state = env.reset()
        done = False
        while not done:
            if done:
                continue
            # Check if the first element of state is a tuple
            if isinstance(state[0], tuple):
                game_state, _ = state  # Unpack the outer tuple
                player_sum, dealer_card, usable_ace = game_state  # Unpack the inner tuple
            else:
                player_sum, dealer_card, usable_ace = state  # Unpack the state
            # Convert state tuple to integer index
            state_index = player_sum + num_player_states * (dealer_card - 1) + num_player_states * num_dealer_states * usable_ace
            action = solution[state_index]
            # Ensure action is either 0 or 1
            action = 0 if action < 0.5 else 1
            step_result = env.step(action)
            # Unpack the step result into five variables
            state, reward, done, usable_ace, info = step_result
            total_reward += reward
            if reward == 1:
                win_count += 1
    return total_reward, win_count

best_fitness = []
# def on_generation(ga_instance):
#     best_fitness.append(ga_instance.best_solution()[1])

def on_generation(ga_instance):
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    total_reward, num_wins = solution_fitness
    win_percentage = num_wins / 100 * 100  # Calculate the win percentage
    print(f"Generation: {ga_instance.generations_completed}, Win Percentage: {win_percentage}%")
    best_fitness.append(total_reward)

game_by_ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=num_parents_mating,
                       num_genes=num_states,
                       init_range_low=0,
                       init_range_high=1,
                       parent_selection_type="sss",
                       keep_parents=1,
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=10,
                       initial_population=initial_population,
                       on_generation=on_generation)

game_by_ga_instance.run()

solution, solution_fitness, solution_idx = game_by_ga_instance.best_solution()
print("Best solution : ", solution)
print("Solution fitness : ", solution_fitness)


# Plot the fitness values
plt.plot(best_fitness)
plt.title('Fitness Evolution')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()