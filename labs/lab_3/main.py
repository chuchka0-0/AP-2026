import argparse

from src.io import read_image, write_image
from src.modifications import SIDES, circle, gradient, halftone
from src.plot import show_images

BACKGROUNDS = {"black": 0, "white": 255}


def parse_arguments() -> argparse.Namespace:
    """
    Разобрать и проверить аргументы командной строки.

    :return: объект с путями к файлам и параметрами
    """
    parser = argparse.ArgumentParser(description="Преобразование изображения.")
    parser.add_argument("image", type=str, help="исходное изображение")
    parser.add_argument("output", type=str, help="файл для результата")
    parser.add_argument(
        "--side",
        type=str,
        choices=SIDES,
        default="right",
        help="сторона, с которой изображение светлее (градиент)",
    )
    parser.add_argument(
        "--background",
        type=str,
        choices=list(BACKGROUNDS),
        default="black",
        help="цвет области вне круга",
    )
    return parser.parse_args()


def main(image_path: str, output_path: str, side: str, background: str) -> None:
    """
    Сделать изображение полутоновым, добавить градиент, сделать круглым
    и сохранить результат.

    :param image_path: путь к исходному изображению
    :param output_path: путь для сохранения результата
    :param side: сторона градиента (left, right, top, bottom)
    :param background: цвет вне круга (black, white)
    """
    try:
        image = read_image(image_path)
        height, width, channels = image.shape

        print(f"Исходное изображение: {image_path}")
        print(f"Размер изображения: {width}x{height}, каналов: {channels}")

        gray = halftone(image)
        grad = gradient(gray, side)
        result = circle(grad, BACKGROUNDS[background])

        show_images(
            {
                "Исходное": image,
                "Полутоновое": gray,
                "Градиент": grad,
                "Круглое": result,
            }
        )

        write_image(output_path, result)
        print(f"Результат сохранён: {output_path}")

    except ValueError as exc:
        print(f"Ошибка: {exc}")
    except OSError as exc:
        print(f"Ошибка при работе с файлом: {exc}")


if __name__ == "__main__":
    args = parse_arguments()
    main(
        image_path=args.image,
        output_path=args.output,
        side=args.side,
        background=args.background,
    )