"""Получение книг с сайта books.toscrape.com."""

from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from books import Book

PAGE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
TIMEOUT = 10


def fetch(url: str) -> requests.Response:
    """Выполняет GET-запрос и проверяет статус ответа.

    param url: адрес запроса
    return: ответ сервера
    raises requests.HTTPError: если статус ответа 4xx/5xx
    """
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response


def parse_book(item, page_url: str) -> Book:
    """Создаёт новую книгу из html-блока.

    param item: блок <article> с книгой (элемент BeautifulSoup)
    param page_url: адрес страницы, на которой найдена книга
    return: новый объект Book
    """
    price_text = item.find("p", class_="price_color").text
    price = "".join(char for char in price_text if char.isdigit() or char == ".")
    return Book(
        title=item.h3.a["title"],
        price=float(price),
        image_url=urljoin(page_url, item.img["src"]),
    )


class BookCatalog:
    """Итерируемый каталог: отдаёт книги со всех страниц сайта."""

    def __iter__(self):
        """Возвращает генератор, который по очереди отдаёт книги."""
        page = 1
        while True:
            try:
                response = fetch(PAGE_URL.format(page))
            except requests.HTTPError as error:
                if error.response.status_code == 404:
                    return
                raise
            soup = BeautifulSoup(response.text, "html.parser")
            for item in soup.find_all("article", class_="product_pod"):
                yield parse_book(item, response.url)
            page += 1