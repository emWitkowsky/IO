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

# inputs = tanks.values[:, :]
# classes = tanks.values[:, 49]
# classes = tanks["Desired tank"].values

data = tanks.drop(tanks.columns[36:49], axis=1)

inputs = data.drop('currentGameTime', axis=1)
classes = data['currentGameTime']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(inputs)

# Standaryzacja danych
# scaled_data = scaler.fit_transform(data)

# PCA
pca = PCA()
pca.fit(X_scaled)

# Wybór liczby komponentów
# np.cumsum(pca.explained_variance_ratio_) - wyjaśniona wariancja w kolejnych komponentach
# Możesz zdecydować, ile komponentów chcesz zachować na podstawie wyjaśnionej wariancji
# Np. pca = PCA(n_components=0.95) - zachowuje komponenty, które wyjaśniają co najmniej 95% wariancji
# Lub pca = PCA(n_components=2) - zachowuje tylko 2 komponenty
pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)

# Wyniki
print(pca_data)