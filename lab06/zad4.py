from keras.applications import ConvNeXtSmall
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, BatchNormalization, GlobalAveragePooling2D
from keras.preprocessing import image_dataset_from_directory
from keras.models import Sequential
from keras.callbacks import History, ModelCheckpoint
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

DATASET = "dogs-cats-mini/"

def train_model(train_data, validation_data, batch_size, image_size):
  base_model = ConvNeXtSmall(input_shape=(*image_size, 3), include_top=False, weights="imagenet")
  base_model.trainable = False

  model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(512, activation="relu"),
    Dropout(0.25),
    Dense(1, activation="sigmoid")
  ])

  history = History()
  checkpoint = ModelCheckpoint('dogs-cats-model.keras', monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
  model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

  model.fit(train_data, validation_data=validation_data, epochs=3, batch_size=batch_size, callbacks=[history, checkpoint])

  return model, history

def calculate_confusion_matrix(model, validation_data):
  all_labels = []
  all_predictions = []
  for data_batch, labels_batch in validation_data:   # all original and predicted labels
    predictions_batch = model.predict_on_batch(data_batch)
    all_labels.extend(labels_batch)
    all_predictions.extend(predictions_batch)

  predicted_classes = np.where(np.array(all_predictions) > 0.5, 1, 0)

  cm = confusion_matrix(all_labels, predicted_classes)

  _, test_acc = model.evaluate(validation_data)
  print(f"Test accuracy: {test_acc * 100:.2f}")   # 80.94%

  return cm

# plotting confusion matrix and learning curves
def plot_diagnostics(history, cm):
  plt.figure(figsize=(10, 7))
  sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
  plt.xlabel('Predicted')
  plt.ylabel('True')
  plt.title('Confusion Matrix')
  plt.savefig("confusion_matrix.png")

  plt.figure(figsize=(10, 5))
  plt.subplot(1, 2, 1)
  plt.plot(history.history['accuracy'], label='Training Accuracy')
  plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.grid(True, linestyle='--', color='grey')
  plt.legend()

  plt.subplot(1, 2, 2)
  plt.plot(history.history['loss'], label='Training Loss')
  plt.plot(history.history['val_loss'], label='Validation Loss')
  plt.xlabel('Epoch')
  plt.ylabel('Loss')
  plt.grid(True, linestyle='--', color='grey')
  plt.legend()

  plt.tight_layout()
  plt.savefig("learning_curve.png")


if __name__ == "__main__":
  image_size = (50, 50)
  batch_size = 32

  train_data = image_dataset_from_directory(
    DATASET,
    validation_split=0.2,
    subset="training",
    seed=288503,
    image_size=image_size,
    batch_size=batch_size
  )

  validation_data = image_dataset_from_directory(
    DATASET,
    validation_split=0.2,
    subset="validation",
    seed=288503,
    image_size=image_size,
    batch_size=batch_size
  )

  trained_model, history = train_model(train_data, validation_data, batch_size, image_size)
  cm = calculate_confusion_matrix(trained_model, validation_data)
  plot_diagnostics(history, cm)

# Model z wcześniejszych laboratoriów: 75.01%
# ConvNeXtSmall ma dokładność 82.3%. Po dotrenowaniu na zdjęciach psów i kotów dało 78.79% (przetrenowaliśmy)
