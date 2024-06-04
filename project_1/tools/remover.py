# Wczytaj plik
with open('merged_output.csv', 'r') as file:
    lines = file.readlines()

# Usuń linie zawierające "Main.js"
lines = [line for line in lines if not any(char.isalpha() for char in line)]

# Zapisz zmodyfikowany plik
with open('../tank_dataset2.csv', 'a') as file:
    file.writelines(lines)

print("Operacja zakończona.")
