import cv2
import numpy as np

def grayscale_avg(image):
    return np.round(np.mean(image, axis=2)).astype(np.uint8)

def grayscale_luminosity(image):
    return np.round(0.299 * image[:,:,2] + 0.587 * image[:,:,1] + 0.114 * image[:,:,0]).astype(np.uint8)

def convert_and_compare(image_path):
    # Wczytaj obraz
    image = cv2.imread(image_path)

    # Konwersja na obraz w skali szarości używając średniej
    gray_avg = grayscale_avg(image)

    # Konwersja na obraz w skali szarości używając wzoru luminancji
    gray_luminosity = grayscale_luminosity(image)

    # Wyświetlenie oryginalnego obrazu oraz obrazów w skali szarości
    cv2.imshow('Original', image)
    cv2.imshow('Grayscale (Average)', gray_avg)
    cv2.imshow('Grayscale (Luminosity)', gray_luminosity)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Testowanie na kilku zdjęciach
image_paths = ['taco.jpg', 'ja.jpg'] # wymagane zmień na rzeczywiste ścieżki

for path in image_paths:
    print("Image:", path)
    convert_and_compare(path)
