''' (6, 14, 15)
6 Сделайте изображение полутоновым.
14 Сделайте изображение круглым (область вне круга должна быть чёрной, белой или прозрачной).
15 Добавьте эффект градиента (изображение с одной из сторон постепенно становится светлее).
'''

import numpy as np
import cv2

SIDES = ("left", "right", "top", "bottom")


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
    :param color: цвет вне круга (0 - чёрный, 255 - белый)
    :return: модифицированное изображение
    """
    if color not in (0, 255):
        raise ValueError("цвет должен быть 0 или 255")

    h, w = image.shape[:2]

    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(mask, (w // 2, h // 2), min(h, w) // 2, 255, -1)

    result = image.copy()
    result[mask == 0] = color
    return result


def gradient(image: np.ndarray, side: str = "right") -> np.ndarray:
    """
    Добавляет эффект градиента: с выбранной стороны изображение
    постепенно становится светлее (у самого края - белое).

    :param image: исходное изображение
    :param side: сторона, где изображение самое светлое:
                 left, right, top или bottom
    :return: модифицированное изображение
    """
    if side not in SIDES:
        raise ValueError(f"сторона должна быть одной из: {', '.join(SIDES)}")

    h, w = image.shape[:2]

    if side in ("left", "right"):
        mask = np.linspace(0, 1, w, dtype=np.float32).reshape(1, w)
        if side == "left":
            mask = mask[:, ::-1]
    else:
        mask = np.linspace(0, 1, h, dtype=np.float32).reshape(h, 1)
        if side == "top":
            mask = mask[::-1, :]

    if image.ndim == 3:
        mask = mask[:, :, np.newaxis]

    img_float = image.astype(np.float32)
    result = img_float + (255.0 - img_float) * mask

    return result.astype(np.uint8)