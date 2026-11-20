"""Гистограмма ужасная"""

import matplotlib.pyplot as plt
import pandas as pd

from dataframe import DOMINANT_COLOR_COLUMN
from image_analysis import CHANNELS

BAR_COLORS = ("red", "green", "blue")

def plot_dominant_color_histogram(df: pd.DataFrame, output_path: str) -> None:
    """Строит, сохраняет и отображает гистограмму доминирующих цветов.

    :param df: DataFrame с колонкой dominant_color
    :param output_path: путь для сохранения графика
    """
    counts = (
        df[DOMINANT_COLOR_COLUMN].value_counts().reindex(CHANNELS, fill_value=0)
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(counts.index, counts.values, color=BAR_COLORS)
    ax.set_title("Распределение доминирующего цвета изображений")
    ax.set_xlabel("Доминирующий цвет")
    ax.set_ylabel("Количество изображений")
    ax.set_yticks(range(0, int(counts.max()) + 2))
    fig.tight_layout()
    fig.savefig(output_path)
    plt.show()