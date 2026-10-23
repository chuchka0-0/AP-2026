"""Книги: модель данных и выбор самых дорогих."""

from typing import Iterable, List, NamedTuple


class Book(NamedTuple):
    """Книга (неизменяемая): название, цена в фунтах и ссылка на обложку."""

    title: str
    price: float
    image_url: str


def most_expensive(books: Iterable[Book], count: int) -> List[Book]:
    """Выбирает самые дорогие книги, не изменяя исходную коллекцию.

    param books: любая коллекция книг
    param count: сколько книг нужно
    return: новый список, отсортированный по убыванию цены
    """
    return sorted(books, key=lambda book: book.price, reverse=True)[:count]