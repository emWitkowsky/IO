# Wczytaj plik
with open('raw.csv', 'r') as file:
    lines = file.readlines()

# Usuń linie zawierające "Main.js"
lines = [line for line in lines if "Main.js" not in line]

# Zapisz zmodyfikowany plik
with open('tank_dataset.csv', 'a') as file:
    file.writelines(lines)

print("Operacja zakończona.")
