import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


df = pd.read_csv("iris.csv")

print(df)

#podział na zbior testowy (30%) i zbior treningowy (70%), ziarno losowości = 13
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)

print(test_set)
print(test_set.shape[0])

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]


# Tworzenie modelu k-NN dla k=3
knn3 = KNeighborsClassifier(n_neighbors=3)

# Tworzenie modelu k-NN dla k=5
knn5 = KNeighborsClassifier(n_neighbors=5)

# Tworzenie modelu k-NN dla k=11
knn11 = KNeighborsClassifier(n_neighbors=11)

# Tworzenie modelu klasyfikatora Naive Bayes
naive_bayes = GaussianNB()

# Trening modeli k-NN dla k=3, k=5, k=11
knn3.fit(train_inputs, train_classes)
knn5.fit(train_inputs, train_classes)
knn11.fit(train_inputs, train_classes)

# Trening modelu klasyfikatora Naive Bayes
naive_bayes.fit(train_inputs, train_classes)

# Predykcja na danych testowych
pred_knn3 = knn3.predict(test_inputs)
pred_knn5 = knn5.predict(test_inputs)
pred_knn11 = knn11.predict(test_inputs)
pred_naive_bayes = naive_bayes.predict(test_inputs)

# Obliczenie dokładności dla każdego modelu
accuracy_knn3 = accuracy_score(test_classes, pred_knn3)
accuracy_knn5 = accuracy_score(test_classes, pred_knn5)
accuracy_knn11 = accuracy_score(test_classes, pred_knn11)
accuracy_naive_bayes = accuracy_score(test_classes, pred_naive_bayes)

print("Dokładność k-NN (k=3): {:.2f}%".format(accuracy_knn3 * 100))
print("Dokładność k-NN (k=5): {:.2f}%".format(accuracy_knn5 * 100))
print("Dokładność k-NN (k=11): {:.2f}%".format(accuracy_knn11 * 100))
print("Dokładność klasyfikatora Naive Bayes: {:.2f}%".format(accuracy_naive_bayes * 100))

# Obliczenie macierzy błędów dla każdego modelu
cm_knn3 = confusion_matrix(test_classes, pred_knn3)
cm_knn5 = confusion_matrix(test_classes, pred_knn5)
cm_knn11 = confusion_matrix(test_classes, pred_knn11)
cm_naive_bayes = confusion_matrix(test_classes, pred_naive_bayes)

print("Macierz błędów dla k-NN (k=3):\n", cm_knn3)
print("\nMacierz błędów dla k-NN (k=5):\n", cm_knn5)
print("\nMacierz błędów dla k-NN (k=11):\n", cm_knn11)
print("\nMacierz błędów dla klasyfikatora Naive Bayes:\n", cm_naive_bayes)

