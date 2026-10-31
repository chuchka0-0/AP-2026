"""Ввод-вывод: скачанные обложки и csv-аннотация."""

import os

import pandas as pd

from path_iterator import ABSOLUTE_COLUMN, RELATIVE_COLUMN
from scrapper import fetch


def download_covers(books, folder: str) -> list:
    """Скачивает обложки всех книг в папку.

    param books: книги (Book)
    param folder: папка для сохранения (создаётся, если её нет)
    return: новый список путей к сохранённым файлам
    """
    os.makedirs(folder, exist_ok=True)
    paths = []
    for number, book in enumerate(books, start=1):
        content = fetch(book.image_url).content
        path = os.path.join(folder, f"{number}.jpg")
        with open(path, "wb") as file:
            file.write(content)
        paths.append(path)
    return paths


def save_annotation(paths, filename: str) -> None:
    """Записывает аннотацию: абсолютный и относительный путь к каждому файлу.

    Относительные пути считаются от текущей рабочей папки.

    param paths: пути к скачанным файлам
    param filename: путь к csv-файлу (недостающие папки создаются)
    """
    directory = os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)
    table = pd.DataFrame(
        {
            ABSOLUTE_COLUMN: [os.path.abspath(path) for path in paths],
            RELATIVE_COLUMN: [os.path.relpath(path) for path in paths],
        }
    )
    table.to_csv(filename, index=False, encoding="utf-8")