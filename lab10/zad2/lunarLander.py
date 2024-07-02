import gymnasium as gym
import pygad


def simulate_game(solution):
    env = gym.make("LunarLander-v2")
    observation, info = env.reset(seed=42)

    for i in range(200):
        action = int(solution[i])
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated:
            env.close()
            return reward

    env.close()
    return reward


def render_game(solution):
    env = gym.make("LunarLander-v2", render_mode="human")
    observation, info = env.reset(seed=42)

    for i in range(200):
        action = int(solution[i])
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated:
            env.close()
            return

    env.close()


# funkcja fitness zwraca nagrodę za grę
def fitness_func(model, solution, solution_idx):
    reward = simulate_game(solution)
    return reward


ga_instance = pygad.GA(
    num_generations=100,
    fitness_func=fitness_func,
    sol_per_pop=200,
    num_parents_mating=100,
    num_genes=200,  # długość chromosomu - długość trasy
    gene_space=[0, 1, 2, 3],  # ruch, który wykonujemy: lewo, dół, prawo, góra
    keep_parents=5,
    parent_selection_type="sss",
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=1,
    stop_criteria=["reach_200"]
)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()

print("Best solution: ", solution)
print("Best solution fitness: ", solution_fitness)

render_game(solution)

# Best solution:  [3. 2. 3. 1. 3. 2. 0. 0. 1. 1. 1. 3. 3. 0. 0. 3. 2. 2. 0. 2. 2. 0. 0. 1.
#  1. 3. 2. 1. 1. 2. 3. 0. 0. 0. 3. 0. 2. 0. 2. 1. 2. 2. 1. 0. 2. 3. 3. 0.
#  0. 2. 3. 2. 1. 0. 2. 1. 2. 3. 1. 2. 1. 1. 3. 0. 2. 0. 2. 0. 3. 0. 3. 3.
#  3. 0. 2. 1. 2. 2. 3. 0. 1. 0. 2. 3. 3. 0. 2. 1. 2. 3. 2. 1. 3. 1. 1. 3.
#  2. 3. 3. 3. 1. 2. 1. 0. 2. 0. 2. 0. 0. 0. 2. 2. 1. 3. 0. 0. 0. 2. 3. 1.
#  1. 2. 0. 3. 2. 3. 0. 2. 0. 0. 3. 1. 3. 3. 2. 3. 1. 0. 2. 3. 3. 2. 2. 1.
#  3. 3. 1. 0. 1. 2. 1. 3. 0. 3. 1. 1. 3. 0. 0. 3. 2. 0. 0. 0. 1. 3. 1. 2.
#  3. 3. 3. 0. 0. 1. 2. 0. 0. 0. 1. 0. 2. 1. 1. 3. 0. 0. 1. 2. 1. 0. 2. 3.
#  1. 3. 0. 0. 3. 2. 3. 3.]
# Best solution fitness:  12.483433797123611