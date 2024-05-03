# from os import makedirs, listdir
# from random import seed, random
# from shutil import copyfile
#
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from keras.src.legacy.preprocessing.image import ImageDataGenerator
# from matplotlib import pyplot
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
# from tensorflow.keras.utils import to_categorical
# from sklearn.metrics import confusion_matrix
# from tensorflow.keras.callbacks import History
# from keras.optimizers import SGD
#
# import sys
# from matplotlib import pyplot
# from keras.utils import to_categorical
# from keras.models import Sequential
# from keras.layers import Conv2D
# from keras.layers import MaxPooling2D
# from keras.layers import Dense
# from keras.layers import Flatten
# from keras.optimizers import SGD
# # from keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# import tensorflow as tf
#
#
#
# # # plot dog photos from the dogs vs cats dataset
# # from matplotlib import pyplot
# # from matplotlib.image import imread
# # # define location of dataset
# # folder = 'dogs-cats-mini'
# # # plot first few images
# # for i in range(9):
# # 	# define subplot
# # 	pyplot.subplot(330 + 1 + i)
# # 	# define filename
# # 	filename = folder + '/dog.' + str(i) + '.jpg'
# # 	print(filename)
# # 	# load image pixels
# # 	image = imread(filename)
# # 	# plot raw pixel data
# # 	pyplot.imshow(image)
# # # show the figure
# # pyplot.show()
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
# # # seed random number generator
# # seed(1)
# # # define ratio of pictures to use for validation
# # val_ratio = 0.25
# # # copy training dataset images into subdirectories
# # src_directory = 'dogs-cats-mini/'
# # for file in listdir(src_directory):
# # 	src = src_directory + '/' + file
# # 	dst_dir = 'train/'
# # 	if random() < val_ratio:
# # 		dst_dir = 'test/'
# # 	if file.startswith('cat'):
# # 		dst = dataset_home + dst_dir + 'cats/' + file
# # 		copyfile(src, dst)
# # 	elif file.startswith('dog'):
# # 		dst = dataset_home + dst_dir + 'dogs/' + file
# # 		copyfile(src, dst)
#
# # opt = SGD(learning_rate=0.001, momentum=0.9)
#
# # define cnn model
# def define_model():
# 	model = Sequential()
# 	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
# 	model.add(MaxPooling2D((2, 2)))
# 	model.add(Flatten())
# 	model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
# 	model.add(Dense(1, activation='sigmoid'))
# 	# compile model
# 	opt = SGD(learning_rate=0.001, momentum=0.9)
# 	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
# 	return model
#
# model = define_model()
#
# # block 1
# model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
# model.add(MaxPooling2D((2, 2)))
# # block 2
# model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
# model.add(MaxPooling2D((2, 2)))
# # block 3
# model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
# model.add(MaxPooling2D((2, 2)))
#
# # create data generator
# # datagen = ImageDataGenerator(rescale=1.0/255.0)
#
# import tensorflow as tf
#
# # Ścieżka do katalogu z danymi
# # data_dir = 'ścieżka/do/katalogu'
#
# # Tworzenie obiektu tf.data.Dataset
# datagen = tf.keras.utils.image_dataset_from_directory(
#     dataset_home,
#     labels='inferred',  # Automatyczne wyznaczenie etykiet na podstawie podkatalogów
#     image_size=(200, 200),  # Rozmiar obrazów
#     batch_size=32,  # Rozmiar batcha
#     shuffle=True  # Losowe przemieszanie danych
# )
#
# # Podział danych na zbiór treningowy i walidacyjny
# # train_dataset = dataset.take(80%)  # Pierwsze 80% danych
# # val_dataset = dataset.skip(80%)  # Pozostałe 20% danych
# # prepare iterators
# train_it = datagen.flow_from_directory('dataset_dogs_vs_cats/train/',
# 	class_mode='binary', batch_size=64, target_size=(200, 200))
# test_it = datagen.flow_from_directory('dataset_dogs_vs_cats/test/',
# 	class_mode='binary', batch_size=64, target_size=(200, 200))
#
# # fit model
# history = model.fit_generator(train_it, steps_per_epoch=len(train_it),
# 	validation_data=test_it, validation_steps=len(test_it), epochs=20, verbose=0)
#
# # evaluate model
# _, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
# print('> %.3f' % (acc * 100.0))
#
# # plot diagnostic learning curves
# def summarize_diagnostics(history):
# 	# plot loss
# 	pyplot.subplot(211)
# 	pyplot.title('Cross Entropy Loss')
# 	pyplot.plot(history.history['loss'], color='blue', label='train')
# 	pyplot.plot(history.history['val_loss'], color='orange', label='test')
# 	# plot accuracy
# 	pyplot.subplot(212)
# 	pyplot.title('Classification Accuracy')
# 	pyplot.plot(history.history['accuracy'], color='blue', label='train')
# 	pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
# 	# save plot to file
# 	filename = sys.argv[0].split('/')[-1]
# 	pyplot.savefig(filename + '_plot.png')
# 	pyplot.close()


import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.applications import Xception
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input, decode_predictions
import numpy as np

# Define the directory path
dataset_home = 'dataset_dogs_vs_cats/'

# Create tf.data.Dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
	dataset_home + 'train/',
	labels='inferred',
	label_mode='binary',  # For binary classification
	image_size=(200, 200),
	batch_size=64,
	shuffle=True
)

test_dataset = tf.keras.utils.image_dataset_from_directory(
	dataset_home + 'test/',
	labels='inferred',
	label_mode='binary',  # For binary classification
	image_size=(200, 200),
	batch_size=64,
	shuffle=True
)


# Define and compile the model
def define_model():
	model = tf.keras.Sequential([
		tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same',
							   input_shape=(200, 200, 3)),
		tf.keras.layers.MaxPooling2D((2, 2)),
		tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'),
		tf.keras.layers.MaxPooling2D((2, 2)),
		tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'),
		tf.keras.layers.MaxPooling2D((2, 2)),
		tf.keras.layers.Flatten(),
		tf.keras.layers.Dense(128, activation='relu', kernel_initializer='he_uniform'),
		tf.keras.layers.Dense(1, activation='sigmoid')
	])

	opt = tf.keras.optimizers.SGD(learning_rate=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])

	return model


keras.applications.Xception(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)


# Define the model
model = define_model()

# Train the model
history = model.fit(train_dataset, validation_data=test_dataset, epochs=3)

# Evaluate the model
_, acc = model.evaluate(test_dataset)
print('> %.3f' % (acc * 100.0))


# Plot learning curves
def summarize_diagnostics(history):
	# Plot loss
	plt.subplot(211)
	plt.title('Cross Entropy Loss')
	plt.plot(history.history['loss'], color='blue', label='train')
	plt.plot(history.history['val_loss'], color='orange', label='test')
	plt.legend()
	# Plot accuracy
	plt.subplot(212)
	plt.title('Classification Accuracy')
	plt.plot(history.history['accuracy'], color='blue', label='train')
	plt.plot(history.history['val_accuracy'], color='orange', label='test')
	plt.legend()
	plt.show()


summarize_diagnostics(history)
