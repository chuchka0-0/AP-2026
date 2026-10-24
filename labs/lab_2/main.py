"""Скачивание обложек самых дорогих книг с books.toscrape.com."""

import argparse
import requests

from book_io import download_covers, save_csv
from books import most_expensive
from scrapper import BookCatalog


def parse_arguments() -> argparse.Namespace:
    """
    Обработка аргументов командной строки.

    return: объект с переданными аргументами командной строки
    """
    parser = argparse.ArgumentParser(
        description="Скачивание обложек самых дорогих книг с books.toscrape.com"
    )
    parser.add_argument(
        "count",
        type=int,
        help="Количество самых дорогих книг, которые нужно скачать",
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default="covers",
        help="Папка для сохранения обложек",
    )
    parser.add_argument(
        "-a",
        "--annotation",
        type=str,
        default="books.csv",
        help="Путь к файлу аннотации (CSV)",
    )
    return parser.parse_args()


def main() -> None:
    """Запускает программу."""
    args = parse_arguments()
    try:

            
        books = most_expensive(BookCatalog(), args.count)
        save_csv(books, args.annotation)
        print("Таблица:", args.annotation)
        for path in download_covers(books, args.directory):
            print("Скачано:", path)


    except ValueError as error:
        print(f"Неверный ввод: {error}")
    except requests.RequestException as error:
        print(f"Ошибка сети: {error}")
    except OSError as error:
        print(f"Ошибка файловой системы: {error}")


if __name__ == "__main__":
    main()
