"""Книги: модель данных и выбор самых дорогих."""


class Book:
    def __init__(self, title: str, price: float, image_url: str):
        """
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
    """
    if count <= 0:
        raise ValueError("Число должно быть положительное.")
    return sorted(books, key=lambda book: book.price, reverse=True)[:count]