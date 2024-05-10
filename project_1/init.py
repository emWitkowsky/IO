import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model

tanks = pd.read_csv("tank_dataset.csv")

# print(df)

last_column = tanks[:, -1]
#podział na zbior testowy (30%) i zbior treningowy (70%), ziarno losowości = 13
(train_set, test_set) = train_test_split(tanks.values, train_size=0.7, random_state=13)

# print(test_set)
# print(test_set.shape[0])

train_inputs = train_set[:, 0:49]
train_classes = train_set[:, 49]
test_inputs = test_set[:, 0:49]
test_classes = test_set[:, 49]

X = tanks.data
y = tanks.target

# Preprocess the data
# Scale the features
# StandardScaler jest narzędziem służącym do skalowania
# cech w zestawie danych w taki sposób,
# że ich średnia jest równa 0, a odchylenie
# standardowe wynosi 1. Jest to rodzaj normalizacji danych
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encode the labels
# encoder = OneHotEncoder(sparse=False)
# Programowanie one hot sluzy do reprezentowania danych kategorycznych
# gdzie kazda klasa reprezentowanie jako wektor zer i jedynek
encoder = OneHotEncoder()
y_encoded = encoder.fit_transform(y.reshape(-1, 1)).toarray()

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(y_encoded.shape[1], activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Pobierz wagi modelu
weights = model.get_weights()

# Wyświetl wagi każdej warstwy
for i in range(len(weights)//2):
    print("Wagi warstwy", i)
    print("Wagi:")
    print(weights[2*i])  # Wagi
    print("Bias:")
    print(weights[2*i + 1])  # Bias
