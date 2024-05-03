import pandas as pd
# import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("iris.csv")

print(df)

#podział na zbior testowy (30%) i zbior treningowy (70%), ziarno losowości = 13
# datasets = train_test_split(df.values, train_size=0.7, random_state=13)

# train_data, test_data, train_labels, test_labels = datasets

#podział na zbior testowy (30%) i zbior treningowy (70%), ziarno losowości = 13
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)

print(test_set)
print(test_set.shape[0])

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]
mlp = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=1000)

mlp.fit(train_inputs, train_classes)

predictions_train = mlp.predict(train_inputs)
print(accuracy_score(predictions_train, train_classes))
predictions_test = mlp.predict(test_inputs)
print(accuracy_score(predictions_test, test_classes))

# Konstrukcja i trenowanie modelu sieci neuronowej
mlp2 = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=2000)

mlp2.fit(train_inputs, train_classes)

# Predykcja na danych treningowych i testowych
predictions_train = mlp2.predict(train_inputs)
train_accuracy = accuracy_score(predictions_train, train_classes)
print("Dokładność na zbiorze treningowym:", train_accuracy)

predictions_test = mlp2.predict(test_inputs)
test_accuracy = accuracy_score(predictions_test, test_classes)
print("Dokładność na zbiorze testowym:", test_accuracy)