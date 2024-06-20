import gym
import numpy as np
import pygad

# Initialize the Blackjack environment
env = gym.make('Blackjack-v1')

# Genetic Algorithm parameters
num_generations = 50
num_parents_mating = 10

# Initialize population with random strategies
num_player_states = 32  # Player sum can be from 0 to 31
num_dealer_states = 10  # Dealer's face-up card can be from 1 to 10
num_ace_states = 2  # Usable ace can be True or False

# The total number of states is the product of the number of states for each observation
num_states = num_player_states * num_dealer_states * num_ace_states

# initial_population = np.random.choice([0, 1], size=(num_parents_mating, num_states))
# Initialize population with random strategies
initial_population = np.random.choice([0, 1], size=(num_parents_mating, num_states))

def fitness_func(ga_instance, solution, solution_idx):
    total_reward = 0
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
    return total_reward

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=num_parents_mating,
                       num_genes=num_states,  # Use num_states instead of env.observation_space.n
                       init_range_low=0,
                       init_range_high=1,
                       parent_selection_type="sss",
                       keep_parents=1,
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=10,
                       initial_population=initial_population)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Best solution : ", solution)
print("Solution fitness : ", solution_fitness)