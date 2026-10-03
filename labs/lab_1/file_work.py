"""Модуль для чтения и записи файлов."""


def read_file(file_path: str) -> str:
    """
    Чтение содержимого файла.

    param file_path: путь читаемого файла
    return: считанный текст из файла
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(file_path: str, txt: str) -> None:
    """
    Запись текста в файл.

    param file_path: путь для записи в файл
    param txt: текст для записи в файл
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(txt)