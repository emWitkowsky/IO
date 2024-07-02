import gymnasium as gym
import pygad


def simulate_game(solution):
    env = gym.make('FrozenLake8x8-v1', is_slippery=False)
    observation, info = env.reset(seed=42)

    for _ in range(20):
        action = solution[observation]
        observation, reward, terminated, truncated, info = env.step(action)

        if reward == 1:
            return (observation, False)

        if terminated:
            return (observation, True)

    env.close()
    return (observation, False)


def render_game(solution):
    env = gym.make('FrozenLake8x8-v1', is_slippery=False, render_mode='human')
    observation, info = env.reset(seed=42)

    for _ in range(20):
        action = int(solution[observation])
        observation, reward, terminated, truncated, info = env.step(action)

        if reward == 1:
            env.close()
            return

    env.close()


def calculate_distance(a, b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])

    return x + y


# karamy za dystans od celu
def fitness_func(model, solution, solution_idx):
    observation, failed = simulate_game(solution)
    column = observation % 8
    row = (observation - column) // 8

    fitness_val = -calculate_distance((row, column), (7, 7))
    if failed:
        fitness_val -= 15

    return fitness_val


ga_instance = pygad.GA(
    num_generations=300,
    num_parents_mating=25,
    fitness_func=fitness_func,
    sol_per_pop=50,
    num_genes=64,
    gene_space=[0, 1, 2, 3],  # lewo, dół, prawo, góra
    keep_parents=5,
    parent_selection_type="rank",
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=5,
    stop_criteria=["reach_0"]
)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Best solution: ", solution)
print("Best solution fitness: ", solution_fitness)

render_game(solution)