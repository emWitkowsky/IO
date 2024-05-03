import cv2
import numpy as np

def grayscale_avg(image):
    return np.round(np.mean(image, axis=2)).astype(np.uint8)

def grayscale_luminosity(image):
    return np.round(0.299 * image[:,:,2] + 0.587 * image[:,:,1] + 0.114 * image[:,:,0]).astype(np.uint8)

def threshold_image(image, threshold=128):
    # Ustaw wartości pikseli na 0 (czarny) lub 255 (biały) w zależności od progu
    thresholded_image = np.where(image >= threshold, 255, 0).astype(np.uint8)
    return thresholded_image

def count_black_points(image):
    # Zsumuj wszystkie piksele o wartości 0 (czarny)
    black_points_count = np.sum(image == 0)
    return black_points_count

def count_connected_components(image):
    norm_image = (image / 255).astype(np.uint8)
    # norm_image = norm_image.astype(np.uint8)
    # Znajdź połączone komponenty w obrazie
    _, labels = cv2.connectedComponents(norm_image)

    # Zwróć liczbę połączonych komponentów, pomniejszoną o 1 (ignorujemy tło)
    return labels.max() - 1

def convert_and_compare(image_path):
    # Wczytaj obraz
    image = cv2.imread(image_path)

    # Konwersja na obraz w skali szarości używając średniej
    gray_avg = grayscale_avg(image)

    # Konwersja na obraz w skali szarości używając wzoru luminancji
    gray_luminosity = grayscale_luminosity(image)

    gray_luminosity_thresholded = threshold_image(gray_luminosity)

    cv2.imshow('Grayscale (Luminosity_thresholded)', gray_luminosity_thresholded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    black_points_count = count_black_points(gray_luminosity_thresholded)
    print("Liczba czarnych punktów:", black_points_count)

    connected_components_count = count_connected_components(gray_luminosity_thresholded)
    print("Liczba połączonych komponentów:", connected_components_count)
    # Konwersja na odcienie szarości
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #
    # # Binaryzacja
    # _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #
    # # Znajdź kontury
    # contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    # # Zlicz czarne plamy
    # black_spots_count = 0
    # for contour in contours:
    #     area = cv2.contourArea(contour)
    #     # Określ próg powierzchni czarnej plamy
    #     if area > 100:
    #         black_spots_count += 1
    #
    # print("Liczba czarnych plam:", black_spots_count)

folder = 'bird_miniatures'

image_paths = ['bird_miniatures/E0071_TR0001_OB0031_T01_M02.jpg', 'bird_miniatures/E0089_TR0005_OB2257_T01_M13.jpg', 'bird_miniatures/E0206_TR0001_OB0020_T01_M10.jpg']

# for image in folder:
for path in image_paths:
    print("Image:", path)
    convert_and_compare(path)


# black_points_count = count_black_points(gray_luminosity_thresholded)
# print("Liczba czarnych punktów:", black_points_count)