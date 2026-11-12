import cv2
import matplotlib.pyplot as plt
import numpy as np


def show_images(images: dict[str, np.ndarray]) -> None:
    """
    Показать изображения в одном окне, в ряд.

    :param images: словарь [подпись, массив изображения]
    :return: None
    """
    plt.figure(figsize=(4 * len(images), 4))

    for i, (title, image) in enumerate(images.items(), start=1):
        plt.subplot(1, len(images), i)
        if image.ndim == 3:
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else:
            plt.imshow(image, cmap="gray", vmin=0, vmax=255)
        plt.title(f"{title}\n{image.shape[1]}x{image.shape[0]}")
        plt.axis("off")
    plt.tight_layout()
    plt.show()