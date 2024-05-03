import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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

clf = DecisionTreeClassifier(random_state=42)
clf.fit(train_inputs, train_classes)

# Predykcja na danych testowych
predictions = clf.predict(test_inputs)

print(predictions)

good_predictions = 0
len = test_set.shape[0]

for i in range(len):
    if predictions[i] == test_classes[i]:
        good_predictions += 1


print(good_predictions)
print(good_predictions/len*100, "%")

# Obliczanie dokładności klasyfikacji
accuracy = accuracy_score(test_classes, predictions)

# Wyświetlanie wyniku jako procentowego udziału poprawnych odpowiedzi
print("Dokładność klasyfikatora: {:.2f}%".format(accuracy * 100))

conf_matrix = confusion_matrix(test_classes, predictions)

print("Macierz błędów:")
print(conf_matrix)


