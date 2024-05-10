# from os import listdir, makedirs
# from random import seed, random
# from shutil import copyfile
#
# from matplotlib import pyplot
# from matplotlib.image import imread
# # define location of dataset
# folder = 'dogs-cats-mini'
# # plot first few images
# for i in range(9):
# 	# define subplot
# 	pyplot.subplot(330 + 1 + i)
# 	# define filename
# 	filename = folder + '/dog.' + str(i) + '.jpg'
# 	print(filename)
# 	# load image pixels
# 	image = imread(filename)
# 	# plot raw pixel data
# 	pyplot.imshow(image)
# # show the figure
# pyplot.show()
#
# # create directories
# dataset_home = 'dataset_dogs_vs_cats/'
# subdirs = ['train/', 'test/']
# for subdir in subdirs:
# 	# create label subdirectories
# 	labeldirs = ['dogs/', 'cats/']
# 	for labldir in labeldirs:
# 		newdir = dataset_home + subdir + labldir
# 		makedirs(newdir, exist_ok=True)
#
# # seed random number generator
# seed(1)
# # define ratio of pictures to use for validation
# val_ratio = 0.25
# # copy training dataset images into subdirectories
# src_directory = 'dogs-cats-mini/'
# for file in listdir(src_directory):
# 	src = src_directory + '/' + file
# 	dst_dir = 'train/'
# 	if random() < val_ratio:
# 		dst_dir = 'test/'
# 	if file.startswith('cat'):
# 		dst = dataset_home + dst_dir + 'cats/' + file
# 		copyfile(src, dst)
# 	elif file.startswith('dog'):
# 		dst = dataset_home + dst_dir + 'dogs/' + file
# 		copyfile(src, dst)
from matplotlib import pyplot as plt
import os
import numpy as np
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

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