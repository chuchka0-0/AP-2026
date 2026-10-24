"""Ввод-вывод: csv-таблица и скачанные обложки."""

import csv
import os
from typing import Iterable, List

from books import Book
from scrapper import fetch


def save_csv(books: Iterable[Book], filename: str) -> None:
    """Записывает книги в csv-файл.

    param books: книги для записи
    param filename: путь к csv-файлу (недостающие папки создаются)
    return: путь к созданному файлу
    """
    directory = os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(Book._fields)
        writer.writerows(books)
    return


def download_covers(books: Iterable[Book], folder: str) -> List[str]:
    """Скачивает обложки всех книг в папку.

    param books: книги
    param folder: папка для сохранения (создаётся, если её нет)
    return: новый список путей к сохранённым файлам
    """
    os.makedirs(folder, exist_ok=True)
    paths = []
    for number, book in enumerate(books, start=1):
        content = fetch(book.image_url).content
        path = os.path.join(folder, f'{number}.jpg')
        with open(path, 'wb') as file:
            file.write(content)
        paths.append(path)
    return paths