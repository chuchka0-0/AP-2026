''' (6, 14, 15) 
6 Сделайте изображение полутоновым.
14 Сделайте изображение круглым (область вне круга должна быть чёрной, белой или прозрачной).

15 Добавьте эффект градиента (изображение с одной из сторон постепенно становится светлее).
''' 

import numpy as np
import cv2

def halftone(image: np.ndarray) -> np.ndarray:
    """
    Делает изображение полутоновым

    :param image: исходное изображение
    :return: модифицированное изображение (полутоновое)
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def circle(image: np.ndarray, color: int = 0) -> np.ndarray:
    """
    Делает изображение круглым

    :param image: исходное изображение
    :param color: цвет вне круга: 0 - чёрный
    :return: модифицированное изображение
    """
    h, w = image.shape[:2]

    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(mask, (w // 2, h // 2), min(h, w) // 2, 255, -1)

    result = image.copy()
    result[mask == 0] = color
    return result
