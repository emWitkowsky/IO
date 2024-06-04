import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score

# Wczytaj dane
tanks = pd.read_csv("tank_dataset.csv")

# print(tanks)

# # Podziel dane na cechy (inputs) i klasy (classes)
# inputs = tanks.values[:, 0:49]
# classes = tanks.values[:, 49]

# Lista indeksów kolumn do usunięcia
# columns_to_drop_indices = [3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 34, 35, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
columns_to_drop_indices = [3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 34, 35, 37,38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]

# Uzyskanie nazw kolumn na podstawie indeksów
columns_to_drop = tanks.columns[columns_to_drop_indices]

# classes = []

# print(len(columns_to_drop))

# Usunięcie kolumn
tanks = tanks.drop(columns_to_drop, axis=1)

# print(tanks.columns)
print(len(tanks.columns))
# data = tanks.drop(tanks.columns[36:49], axis=1)
data = tanks
# print(data.columns)
# print(len(data.columns))
inputs = tanks.values[:, 0:13]
classes = tanks.values[:, 13]

# Przeskaluj cechy
scaler = StandardScaler()
X_scaled = scaler.fit_transform(inputs)

# Zakoduj klasy
encoder = OneHotEncoder()
y_encoded = encoder.fit_transform(classes.reshape(-1, 1)).toarray()

# print("yes")

# Podziel dane na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)

print("test")

# Zdefiniuj model drzewa decyzyjnego
decision_tree = DecisionTreeClassifier(max_depth=4)

# Trenuj model drzewa decyzyjnego na danych treningowych
decision_tree.fit(X_train, y_train)

print("test")

# Przewiduj klasy dla danych testowych
y_pred = decision_tree.predict(X_test)

# Oblicz dokładność modelu
accuracy = accuracy_score(y_test, y_pred)
print("Dokładność modelu drzewa decyzyjnego:", accuracy)

# Wizualizuj strukturę drzewa
# plt.figure(figsize=(20, 10))
# plot_tree(decision_tree, filled=True, feature_names=tanks.columns[:-1], class_names=encoder.categories_[0])
# plt.show()

tree_rules = export_text(decision_tree, feature_names=data.columns[:-1].tolist())
print(tree_rules)

# Pobierz elementy drzewa
n_nodes = decision_tree.tree_.node_count
children_left = decision_tree.tree_.children_left
children_right = decision_tree.tree_.children_right
feature = decision_tree.tree_.feature
threshold = decision_tree.tree_.threshold

# # Rekurencyjna funkcja wyodrębniająca reguły i zapisująca je do pliku
# def print_rules(node, depth, file):
#     indent = "  " * depth
#     if children_left[node] != children_right[node]:  # jeśli nie jest liściem
#         file.write(f"{indent}if (feature[{feature[node]}] <= {threshold[node]:.2f}) {{\n")
#         print_rules(children_left[node], depth + 1, file)
#         file.write(f"{indent}}} else {{  // if (feature[{feature[node]}] > {threshold[node]:.2f})\n")
#         print_rules(children_right[node], depth + 1, file)
#         file.write(f"{indent}}}\n")
#     else:
#         file.write(f"{indent}return 'class {decision_tree.classes_[np.argmax(decision_tree.tree_.value[node])]}';\n")
# def print_rules(node, depth, file):
#     indent = "  " * depth
#     if depth < 4:  # Sprawdź głębokość drzewa
#         if children_left[node] != children_right[node]:  # jeśli nie jest liściem
#             file.write(f"{indent}if (feature[{feature[node]}] <= {threshold[node]:.2f}) {{\n")
#             print_rules(children_left[node], depth + 1, file)
#             file.write(f"{indent}}} else {{  // if (feature[{feature[node]}] > {threshold[node]:.2f})\n")
#             print_rules(children_right[node], depth + 1, file)
#             file.write(f"{indent}}}\n")
#         else:
#             file.write(f"{indent}return 'class {decision_tree.classes_[np.argmax(decision_tree.tree_.value[node])]}';\n")
#     else:
#         file.write(f"{indent}return 'class {decision_tree.classes_[np.argmax(decision_tree.tree_.value[node])]}';\n")

def print_rules(node, depth, file):
    indent = "  " * depth
    if depth < 4:  # Sprawdź głębokość drzewa
        if children_left[node] != children_right[node]:  # jeśli nie jest liściem
            file.write(f"{indent}if (feature[{feature[node]}] <= {threshold[node]:.2f}) {{\n")
            print_rules(children_left[node], depth + 1, file)
            file.write(f"{indent}}} else {{  // if (feature[{feature[node]}] > {threshold[node]:.2f})\n")
            print_rules(children_right[node], depth + 1, file)
            file.write(f"{indent}}}\n")
        else:
            # Zwróć rzeczywistą klasę dla danego liścia
            leaf_class = decision_tree.predict([X_train[node]])[0]
            file.write(f"{indent}return 'class {leaf_class}';\n")
    else:
        # Zwróć rzeczywistą klasę dla danego liścia
        leaf_class = decision_tree.predict([X_train[node]])[0]
        file.write(f"{indent}return 'class {leaf_class}';\n")

# Otwarcie pliku if.js do zapisu
with open("if.js", "w") as file:
    # Opcjonalnie można dodać jakiś nagłówek do pliku
    file.write("// Reguły drzewa decyzyjnego\n\n")
    print_rules(0, 0, file)
