"""Книги: модель данных и выбор самых дорогих."""


class Book:
    """Книга: название, цена в фунтах и ссылка на обложку."""

    def __init__(self, title: str, price: float, image_url: str):
        """Создаёт книгу.

        param title: название книги
        param price: цена в фунтах
        param image_url: ссылка на обложку
        """
        self.title = title
        self.price = price
        self.image_url = image_url


def most_expensive(books, count: int) -> list:
    """Выбирает самые дорогие книги, не изменяя исходную коллекцию.

    param books: любая коллекция книг (Book)
    param count: сколько книг нужно
    return: новый список, отсортированный по убыванию цены
    raises ValueError: если count не является положительным числом
    """
    if count <= 0:
        raise ValueError("Число должно быть больше нуля")
    return sorted(books, key=lambda book: book.price, reverse=True)[:count]