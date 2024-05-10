import os
import numpy as np
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from keras.optimizers import Adam

# Define directory and classes
data_dir = 'dataset_dogs_vs_cats/'

# Get list of image paths
image_paths = [os.path.join(data_dir, fname) for fname in os.listdir(data_dir) if fname.endswith('.jpg')]

# Extract labels from filenames
labels_names = ['cat' if 'cat' in fname else 'dog' for fname in os.listdir(data_dir) if fname.endswith('.jpg')]
labels = [1 if label=='cat' else 0 for label in labels_names]
# Load images and convert them to arrays
images = [img_to_array(load_img(img_path, target_size=(64, 64))) for img_path in image_paths]

# Convert list of arrays to a single array
images = np.array(images)

# Normalize image data to [0, 1] range
images /= 255.

# Split data into training and validation sets

X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=288478)

y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
original_test_labels = np.argmax(y_val, axis=1)

# Create data generators
datagen = ImageDataGenerator()

datagen_augmented = ImageDataGenerator(
    rotation_range=20,       # randomly rotate images in the range (degrees, 0 to 180)
    width_shift_range=0.1,   # randomly shift images horizontally (fraction of total width)
    height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
    shear_range=0.2,         # set range for random shear
    zoom_range=0.2,          # set range for random zoom
    horizontal_flip=True,    # randomly flip images
    fill_mode='nearest'      # set mode for filling points outside the input boundaries
)

#train_it = datagen.flow(X_train, y_train, batch_size=64)
train_it_augmented = datagen_augmented.flow(X_train, y_train, batch_size=64)
val_it = datagen.flow(X_val, y_val, batch_size=64)

# Define the model
model = Sequential()

model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64, activation='sigmoid'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()
model.save('champion_dogcat.h5')

# Train the model
history = model.fit(train_it_augmented, validation_data=val_it, epochs=100)

predictions = model.predict(images)

# Get the indices of images that have a probability around 50% (±2%)
indices = np.where((predictions >= 0.48) & (predictions <= 0.52))[0]

# Get the corresponding image paths
selected_image_paths = [image_paths[i] for i in indices]

# Print the selected image paths
#print(selected_image_paths)

# Plot training & validation accuracy values
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.tight_layout()
plt.show()
plt.savefig('RESULTS!.png')