"""Итератор по путям к файлам."""

import os

import pandas as pd

ABSOLUTE_COLUMN = "absolute_path"
RELATIVE_COLUMN = "relative_path"


class PathIterator:
    """Итератор по путям к файлам.

    Источником может быть csv-файл аннотации или путь к папке.
    Для аннотации отдаются абсолютные пути из неё, для папки — абсолютные
    пути всех файлов, лежащих в этой папке.
    """

    def __init__(self, source: str):
        """Создаёт итератор.

        param source: путь к csv-файлу аннотации или к папке с файлами
        raises FileNotFoundError: если такого файла или папки нет
        """
        if os.path.isdir(source):
            self._paths = self._read_folder(source)
        elif os.path.isfile(source):
            self._paths = self._read_annotation(source)
        else:
            raise FileNotFoundError(f"Не найден файл или папка: {source}")
        self._index = 0

    @staticmethod
    def _read_folder(folder: str) -> list:
        """Собирает абсолютные пути файлов папки.

        param folder: путь к папке
        return: список путей (1.jpg, 2.jpg, ... 10.jpg в числовом порядке)
        """
        names = [
            name for name in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, name))
        ]
        names.sort(key=lambda name: (len(name), name))
        return [os.path.abspath(os.path.join(folder, name)) for name in names]

    @staticmethod
    def _read_annotation(filename: str) -> list:
        """Читает абсолютные пути из файла аннотации.

        param filename: путь к csv-файлу аннотации
        return: список абсолютных путей
        """
        table = pd.read_csv(filename, encoding="utf-8")
        return table[ABSOLUTE_COLUMN].tolist()

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self) -> str:
        """Возвращает следующий путь.

        return: путь к файлу
        raises StopIteration: когда пути закончились
        """
        if self._index >= len(self._paths):
            raise StopIteration
        path = self._paths[self._index]
        self._index += 1
        return path