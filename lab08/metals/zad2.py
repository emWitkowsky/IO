import pygad
import math

def endurance(x, y, z, u, v, w):
  return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

def fitness_func(model, solution, solution_idx):
  x, y, z, u, v, w = solution
  return endurance(x, y, z, u, v, w)

gene_space = [i * 0.01 for i in range(100)]

ga_instance = pygad.GA(
  num_generations=100,
  sol_per_pop=100,
  num_parents_mating=100//2,
  gene_space=gene_space,
  num_genes=6,
  mutation_percent_genes=15,
  fitness_func=fitness_func
)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution: {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
ga_instance.plot_fitness().savefig("plot.png")

# Najlepsza wytrzymałość dla stopu metali to ~2.83.

# Trzeba zmieszać metale w ilościach około [0.53 0.51 0.99 0.99 0.21 0.01].

# Wartości, które mi wychodziły w różnych próbach:
# Parameters of the best solution : [0.38 0.38 0.99 0.99 0.   0.05]
# Fitness value of the best solution = 2.830388206433966

# Parameters of the best solution : [0.53 0.51 0.99 0.99 0.21 0.01]
# Fitness value of the best solution = 2.8305109623093703

# Parameters of the best solution : [0.53 0.51 0.99 0.99 0.21 0.01]
# Fitness value of the best solution = 2.8305109623093703

# Parameters of the best solution : [0.71 0.65 0.99 0.99 0.14 0.  ]
# Fitness value of the best solution = 2.8305463431843645