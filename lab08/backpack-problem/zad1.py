import pygad
import time

items = [
    {"name": "zegar", "weight": 7, "value": 100},
    {"name": "obraz-pejzaz", "weight": 7, "value": 300},
    {"name": "obraz-portret", "weight": 6, "value": 400},
    {"name": "radio", "weight": 2, "value": 40},
    {"name": "laptop", "weight": 5, "value": 500},
    {"name": "lampka-nocna", "weight": 6, "value": 70},
    {"name": "srebrne-sztucce", "weight": 1, "value": 100},
    {"name": "porcelana", "weight": 3, "value": 250},
    {"name": "figura-z-bronzu", "weight": 10, "value": 300},
    {"name": "skorzana-torebka", "weight": 3, "value": 280},
    {"name": "odkurzacz", "weight": 15, "value": 300}
]

max_capacity = 25
best_expected_solution = 1630


def fitness_function(model, solution, solution_idx):
    total_weight = sum(item["weight"] for item, selected in zip(items, solution) if selected)
    total_value = sum(item["value"] for item, selected in zip(items, solution) if selected)

    if total_weight > max_capacity or total_value > best_expected_solution:
        return 0

    return total_value


def on_generation(ga_instance):
    best_solution = ga_instance.best_solution()
    best_solution_fitness = best_solution[1]
    if best_solution_fitness >= best_expected_solution:
        ga_instance.keep_solving = False


solutions_count = 0
total_successful_time = 0


for i in range(10):
    start_time = time.time()

    ga_instance = pygad.GA(
        fitness_func=fitness_function,
        gene_type=int,
        gene_space=[0, 1],
        num_generations=50,
        num_parents_mating=2,
        sol_per_pop=10,
        parent_selection_type="sss",
        crossover_type="single_point",
        mutation_type="random",
        num_genes=len(items),
        on_generation=on_generation
    )

    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()

    selected_items = [item["name"] for item, selected in zip(items, solution) if selected]
    total_weight = sum(item["weight"] for item, selected in zip(items, solution) if selected)
    total_value = sum(item["value"] for item, selected in zip(items, solution) if selected)

    print(f"Solution: {selected_items}")
    print(f"Total value: {total_value}")
    print(f"Total weight: {total_weight}")
    total_time = time.time() - start_time

    if solution_fitness >= best_expected_solution:
        solutions_count += 1
        total_successful_time += total_time

    ga_instance.plot_fitness().savefig(f"fitness-plot{i}.png")

print(f"Best solutions: {solutions_count / 10 * 100}%")
if solutions_count > 0:
    print(f"Average time of successful solution: {total_successful_time / solutions_count} seconds")
else:
    print("There was no successful solution.")

# a) Sensowna będzie lista

# b) W kontekście problemu plecakowego, sensowna funkcja fitness powinna maksymalizować wartość w plecaku,
# nie przekraczając jego maksymalnej pojemności. W moim przypadku oblicza sumę wag wszystkich przedmiotów
# wybranych do plecaka, oblicza sumę wartości tych przedmiotów i sprawdza, czy suma wag przekracza 25 kg
# i czy suma wartości przekracza 1630. Jeśli tak, to zwraca 0 - wynik jest odrzucony. Jeśli nie,
# funkcja zwraca sumę wartości. To oznacza, że im większa wartość przedmiotów w plecaku, tym lepszy wynik.
# Może kary by sie szybciej uczyl???

# c) Trzeba znaleźć odpowiednią liczbę pokoleń, aby nie doprowadzić do nieznalezienia optymalnego rozwiązania
# lub niepotrzebnego zużycia zasobów. 50 pokoleń wydawaje się dobrym strzałem.
# Liczba rodziców biorących udział w krzyżowaniu - wybrano typowo, 2 rodziców, ale więcej może zwiększyć
# różnorodność populacji, więc też warto próbować.
# Ogółem ważne jest, by parametry nie miały ani za małych, ani za dużych wartości. Np. zbyt mała populacja
# może prowadzić do braku różnorodności, ale duża zużyje zasoby.

# d) Powinniśmy zabrać: Zegar (100), Obraz portret (400), Laptop (500), Srebrne Sztućce (100), Porcelanę (250),
# Skórzaną torebkę (280).

# e) 50% (5) znalazło najlepsze rozwiązanie

# f) Średni czas w przypadku znalezienia najlepszego rozwiązania wynosi 0.01046004295349121 seconds