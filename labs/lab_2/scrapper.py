"""Получение книг с сайта books.toscrape.com."""

import re
from typing import Iterator
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

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


def parse_book(item: Tag, page_url: str) -> Book:
    """Создаёт новую книгу из html-блока.

    param item: блок <article> с книгой
    param page_url: адрес страницы, на которой найдена книга
    return: новый объект Book
    """
    price_text = item.find("p", class_="price_color").text
    return Book(
        title=item.h3.a["title"],
        price=float(re.sub(r"[^\d.]", "", price_text)),
        image_url=urljoin(page_url, item.img["src"]),
    )
"""
class BookIterator:
    def __init__(self, filename: Path):"""
        

class BookCatalog:
    """Итерируемый каталог: отдаёт книги со всех страниц сайта."""

    def __iter__(self) -> Iterator[Book]:
        """Возвращает итератор, который по очереди отдаёт книги."""
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
