"""Скачивание обложек самых дорогих книг с books.toscrape.com."""

import requests

from book_io import download_covers, save_csv
from books import most_expensive
from scrapper import BookCatalog


def ask_count() -> int:
    """Спрашивает у пользователя количество книг.

    :return: положительное целое число
    :raises ValueError: если введено не положительное число
    """
    count = int(input('Сколько самых дорогих книг скачать? '))
    if count <= 0:
        raise ValueError('число должно быть больше нуля')
    return count


def main() -> None:
    """Запускает программу."""
    try:
        books = most_expensive(BookCatalog(), ask_count())
        print('Таблица:', save_csv(books, 'books.csv'))
        for path in download_covers(books, 'covers'):
            print('Скачано:', path)
    except ValueError as error:
        print(f'Неверный ввод: {error}')
    except requests.RequestException as error:
        print(f'Ошибка сети: {error}')


if __name__ == '__main__':
    main()