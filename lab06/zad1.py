from apyori import apriori
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

titanic_data = pd.read_csv('titanic.csv', header=None)

# print(titanic_data)

items = []

for i in range(len(titanic_data)):
    items.append([str(titanic_data.values[i, j]) for j in range(1, 5)])

final_rule = apriori(items, min_support=0.005, min_confidence=0.8)
final_results = list(final_rule)

# print(final_results)

# Posortowanie reguł według ufności
sorted_results = sorted(final_results, key=lambda x: x.ordered_statistics[0].confidence, reverse=True)

# Wyświetlenie posortowanych reguł
for result in sorted_results:
    print("Items:", result.items)
    print("Support:", result.support)
    print("Confidence:", result.ordered_statistics[0].confidence)
    print("Lift:", result.ordered_statistics[0].lift)
    print("--------------------")

# Tworzenie listy słowników z danymi reguł
data = []
for result in sorted_results:
    data.append({
        'Items': ", ".join(result.items),
        'Support': result.support,
        'Confidence': result.ordered_statistics[0].confidence,
        'Lift': result.ordered_statistics[0].lift
    })


df = pd.DataFrame(data)

# Wykres słupkowy dla wsparcia
df.plot(kind='bar', x='Items', y='Support', figsize=(10, 6), title='Support for Rules')

# Wykres słupkowy dla ufności
df.plot(kind='bar', x='Items', y='Confidence', figsize=(10, 6), title='Confidence for Rules')

# Wykres słupkowy dla podniesienia (lift)
df.plot(kind='bar', x='Items', y='Lift', figsize=(10, 6), title='Lift for Rules')

# Wyświetlenie wykresów
plt.show()
