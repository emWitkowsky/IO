import pandas as pd
# import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

df = pd.read_csv("diabetes1.csv")

print(df)

label_encoder = LabelEncoder()
df['class'] = label_encoder.fit_transform(df['class'])

#podział na zbior testowy (30%) i zbior treningowy (70%), ziarno losowości = 13
# datasets = train_test_split(df.values, train_size=0.7, random_state=13)

# train_data, test_data, train_labels, test_labels = datasets

#podział na zbior testowy (30%) i zbior treningowy (70%), ziarno losowości = 13
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)

train_inputs = train_set[:, 0:8]
train_classes = train_set[:, 8]
test_inputs = test_set[:, 0:8]
test_classes = test_set[:, 8]

# mlp_model = MLPClassifier(hidden_layer_sizes=(6, 3), activation='relu', max_iter=500)
mlp_model = MLPClassifier(hidden_layer_sizes=(3, 3), activation='identity', max_iter=500)
mlp_model.fit(train_inputs, train_classes)

# Przewidywanie na zbiorze testowym
predictions = mlp_model.predict(test_inputs)

# Ocena dokładności modelu
accuracy = accuracy_score(test_classes, predictions)
print("Dokładność modelu: {:.2f}".format(accuracy))

conf_matrix = confusion_matrix(test_classes, predictions)

print("Macierz błędu:")
print(conf_matrix)

# # Get the elements of the confusion matrix
# TN, FP, FN, TP = conf_matrix.ravel()
#
# # Reformat the confusion matrix
# conf_matrix_formatted = [[TN, FP], [FN, TP]]
#
# print(conf_matrix_formatted)

# Gorsze są FN, bo usypiają naszą czujność myśląc że jesteśmy zdrowi