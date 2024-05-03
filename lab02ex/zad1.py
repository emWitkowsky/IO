import pandas as pd
import numpy as np

# Wczytanie pliku CSV
df = pd.read_csv("iris_with_errors.csv")

# Wykrywanie brakujących wartości
missing_values_count = df.isnull().sum()

# Wyświetlanie liczby brakujących wartości
print("Liczba brakujących lub nieuzupełnionych danych:")
print(missing_values_count)

# Wyświetlanie statystyk bazy danych
print("\nStatystyki bazy danych:")
print(df.describe())