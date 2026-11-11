import cv2
import numpy as np


def read_image(path_image: str) -> np.ndarray:
    """
    Считывает изображение из файла.

    :param path_image: путь к изображению
    :return: изображение
    """
    image = cv2.imread(path_image)
    if image is None:
        raise FileNotFoundError(f"не удалось прочитать изображение: {path_image}")
    return image


def write_image(path_image: str, image: np.ndarray) -> None:
    """
    Сохраняет изображение в файла.

    :param path_image: путь к изображению
    :param image: изображение
    """
    if not cv2.imwrite(path_image, image):
        raise OSError(f"не удалось сохранить изображение: {path_image}")
