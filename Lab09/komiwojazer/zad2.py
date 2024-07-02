import matplotlib.pyplot as plt
import random, time
from aco import AntColony

plt.style.use("dark_background")

COORDS = (
  (20, 52), (43, 50), (20, 84), (70, 65), (29, 90),
  (87, 83), (73, 23), (10, 20), (40, 60), (60, 80),
  (30, 40), (50, 70), (90, 30), (20, 40), (80, 50),
  (60, 90), (40, 30), (50, 10), (70, 20), (90, 90),
)

def random_coord():
  r = random.randint(0, len(COORDS))
  return r


def plot_nodes(w=12, h=8):
  for x, y in COORDS:
    plt.plot(x, y, "g.", markersize=15)
  plt.axis("off")
  fig = plt.gcf()
  fig.set_size_inches([w, h])


def plot_all_edges():
  paths = ((a, b) for a in COORDS for b in COORDS)

  for a, b in paths:
    plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

# oryginalny zestaw
colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2,
                   pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                   iterations=300)

# eksperyment 1: 500 mrówek, 300 iteracji, zwiekszenie znaczenia feromonów (alpha)
colony = AntColony(COORDS, ant_count=500, alpha=1.0, beta=1.2,
                   pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                   iterations=300)

# eksperyment 2: 250 mrówek, 250 iteracji, zmniejszenie współczynnika ewaporacji, alpha 1.0
colony = AntColony(COORDS, ant_count=250, alpha=1.0, beta=1.2,
                   pheromone_evaporation_rate=0.20, pheromone_constant=1000.0,
                   iterations=250)

# eksperyment 3: 400 mrówek, 400 iteracji, większy współczynnik ewaporacji, alpha 0.5
colony = AntColony(COORDS, ant_count=400, alpha=0.5, beta=1.2,
                   pheromone_evaporation_rate=0.60, pheromone_constant=1000.0,
                   iterations=400)

optimal_nodes = colony.get_path()

for i in range(len(optimal_nodes) - 1):
  plt.plot(
    (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
    (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
  )

plt.show()

# oryginalny zestaw danych: fig-1.png, dł trasy ~231.55, 32.23 sekundy
# oryginalny zestaw, 20 wierzchołków: fig-2.png, dł trasy ~494.14, 2min 12s 24ms
# eksperyment 1: fig-3.png, dł trasy ~484.44, 3.48min
# eksperyment 2: fig-4.png, dł trasy ~494.52, 1min 11s 56ms
# eksperyment 3: fig-5.png, dł trasy ~484.32, 4min 21s 61ms

# Wnioski:
# Mrówki wolą mniejsze liczby wierzchołków, co jest zrozumiałe, bo łatwiej im znaleźć najkrótszą trasę.
# Więcej wierzchołków = więcej czasu
# 400 mrówek w 400 iteracjach to zbyt dużo, nie ma sensu, bo wykonywało się to prawie 5 minut, a raczej cenimy czas
# Warto zwiększyć znaczenie feromonów, bo w eksperymencie 1 uzyskano lepsze wyniki niż w oryginalnym zestawie
# danych, ale wciąż nie były one zadowalające.