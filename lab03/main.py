import pandas as pd
# import sklearn
from sklearn.model_selection import train_test_split

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

def classify_iris(sl, sw, pl, pw):
    if pl < 2 and pw < 1:
        return "Setosa"
    elif sl >= 6 and pl > 5:
        return "Virginica"
    else:
        return "Versicolor"

good_predictions = 0
len = test_set.shape[0]


sorted_test_set = test_set[test_set[:, 4].argsort()]
print(sorted_test_set)



for i in range(len):
    prediction = classify_iris(test_inputs[i, 0], test_inputs[i, 1], test_inputs[i, 2], test_inputs[i, 3])
    if prediction == test_classes[i]:
        good_predictions += 1


print(good_predictions)
print(good_predictions/len*100, "%")