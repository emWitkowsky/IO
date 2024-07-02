import math
import numpy as np
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

# a) prosta optymalizacja

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

# b) dodanie ograniczeń:
x_min = [1, 1]
x_max = [2, 2]
my_bounds = (x_min, x_max)


# optymizer z uzyciem funkcji sphere
# optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options, bounds=my_bounds)
# optimizer.optimize(fx.sphere, iters=1000)

# best cost: 2.0602938626445084, best pos: [1.004536   1.02528108]

# c) dostosowanie do problemu inżynieryjnego

def endurance(list_of_params):
  x, y, z, u, v, w = list_of_params
  return -(math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w))

x_max = np.ones(6) # ustawienie dim na 6
x_min = np.zeros(6) # ustawienie dim na 6
my_bounds = (x_min, x_max) # ustawienie dim na 6

# d) zmiana fx na endurance, f dla całego roju

def f(swarm):
  return np.array([endurance(p) for p in swarm]) # funkcja która przebiegnie przez cały rój

optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)
optimizer.optimize(f, iters=1000) # wrzucamy funkcję f do optymalizatora

# f) wykres kosztu

cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()

# best cost: -2.8128296030930193, best pos: [0.71755627 0.57490464 0.98731302 0.98548728 0.03230467 0.57641782]

