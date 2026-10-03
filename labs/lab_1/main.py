import argparse
import os

from file_work import read_file, write_file
from prof import filter_profiles, parse_profiles


def parse_arguments() -> argparse.Namespace:
    """
    Обработка аргументов командной строки.

    return: объект с переданными аргументами командной строки
    """
    parser = argparse.ArgumentParser(
        description="Подсчёт кол-ва людей с фамилиями на ов/ова"
    )
    parser.add_argument("input", type=str, help="Файл с исходными данными")
    parser.add_argument(
        "-o", "--output", type=str, default="result.txt", help="Файл с результатами"
    )
    return parser.parse_args()


def main() -> None:
    """
    Чтение анкет, отбор нужных, вывод количества и сохранение в файл.
    """
    args = parse_arguments()

    if os.path.abspath(args.input) == os.path.abspath(args.output):
        print("Ошибка: входной и выходной файлы совпадают")
        return

    try:
        text = read_file(args.input)
        profiles = parse_profiles(text)
        if not profiles:
            print("Ошибка: в файле нет анкет")
            return
        found = filter_profiles(profiles)
        write_file(args.output, "\n\n".join(found))
    except OSError as exc:
        print(f"Ошибка при работе с файлом: {exc}")
        return

    print(f"Найдено людей с фамилиями на ов/ова: {len(found)}\n")
    print("\n\n".join(found))
    print(f"\nАнкеты сохранены в файл: {args.output}")


if __name__ == "__main__":
    main()
