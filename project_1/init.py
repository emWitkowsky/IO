import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from tensorflow.keras.layers import Input, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import plot_model

tanks = pd.read_csv("tank_dataset2.csv")

# Lista indeksów kolumn do usunięcia
# columns_to_drop_indices = [3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 34, 35, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
columns_to_drop_indices = [3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 34, 35, 37,38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]

# Uzyskanie nazw kolumn na podstawie indeksów
columns_to_drop = tanks.columns[columns_to_drop_indices]

# Usunięcie kolumn
tanks = tanks.drop(columns_to_drop, axis=1)

# data = tanks.drop(tanks.columns[36:49], axis=1)
data = tanks
print(data.columns)
print(len(data.columns))

# inputs = tanks.values[:, :]
# classes = tanks.values[:, 49]
# classes = tanks["Desired tank"].values

inputs = data.drop('currentGameTime', axis=1)
classes = data['currentGameTime']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(inputs)

# Standaryzacja danych
# scaled_data = scaler.fit_transform(data)

# # PCA
# pca = PCA()
# pca.fit(X_scaled)
#
# # Wybór liczby komponentów
# # np.cumsum(pca.explained_variance_ratio_) - wyjaśniona wariancja w kolejnych komponentach
# # Możesz zdecydować, ile komponentów chcesz zachować na podstawie wyjaśnionej wariancji
# # Np. pca = PCA(n_components=0.95) - zachowuje komponenty, które wyjaśniają co najmniej 95% wariancji
# # Lub pca = PCA(n_components=2) - zachowuje tylko 2 komponenty
# pca = PCA(n_components=2)
# pca_data = pca.fit_transform(X_scaled)
#
# # Wyniki
# print(pca_data)

print(X_scaled.shape[1])

# Define the model
model = Sequential([
    Input(shape=(X_scaled.shape[1],)),
    Dense(5, activation='relu'),
    # Dense(y_encoded.shape[1], activation='softmax')
    Dense(1, activation='sigmoid')
])
# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Trenuj model na całym zestawie danych
model.fit(X_scaled, classes, epochs=20, batch_size=64)

# Pobierz wagi i obciążenia dla każdej warstwy
weights1, bias1 = model.layers[0].get_weights()
weights2, bias2 = model.layers[1].get_weights()

# Wyświetl kształt wag i obciążeń dla pierwszej warstwy
print("Shape of weights1:", weights1.shape)
print("Shape of bias1:", bias1.shape)

# Wyświetl kształt wag i obciążeń dla drugiej warstwy
print("Shape of weights2:", weights2.shape)
print("Shape of bias2:", bias2.shape)

weights1_list = weights1.tolist()
bias1_list = bias1.tolist()
weights2_list = weights2.tolist()
bias2_list = bias2.tolist()

# Zapisz dane do pliku "wagi_WRONG.py"
with open("wagi.py", "w") as file:
    file.write("# Wagi i obciazenia dla pierwszej warstwy\n")
    file.write("weights1 = " + str(weights1_list) + "\n")
    file.write("bias1 = " + str(bias1_list) + "\n")
    file.write("# Wagi i obciazenia dla drugiej warstwy\n")
    file.write("weights2 = " + str(weights2_list) + "\n")
    file.write("bias2 = " + str(bias2_list) + "\n")

print("Dane zostały zapisane do pliku wagi.py")
