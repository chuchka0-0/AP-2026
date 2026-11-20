"""Вариант 6: определение доминирующего цвета (на основе значения яркости цвета)."""

import cv2
import numpy as np

CHANNELS = ("r", "g", "b")


def dominant_color(image_path: str) -> str:
    """Определяет доминирующий цвет изображения. (если цвета равны, по порыдку (r, g, b))

    :param image_path: путь к изображению
    :return: цвет
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Не удалось прочитать изображение: {image_path}")
    means_bgr = image.mean(axis=(0, 1))
    means_rgb = means_bgr[::-1]
    return CHANNELS[np.max(means_rgb)]