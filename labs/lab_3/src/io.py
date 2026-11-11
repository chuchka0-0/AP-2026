import cv2
import numpy as np

def read_image(path_image: str) -> np.ndarray:
    image = cv2.imread(path_image)
    if image is None:
        raise FileNotFoundError(f"не удалось прочитать изображение: {path_image}")
    return image

def write_image(path_image: str, image: np.ndarray) -> np.ndarray:
    if not cv2.imwrite(path_image, image):
        raise OSError(f"не удалось сохранить изображение: {path_image}")