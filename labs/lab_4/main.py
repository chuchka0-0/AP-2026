import argparse

from src.dataframe import (
    add_dominant_color,
    filter_by_dominant_color,
    load_annotation,
    sort_by_dominant_color,
)
from src.image_analysis import CHANNELS
from src.plot import plot_dominant_color_histogram


def parse_args() -> argparse.Namespace:
    """Разбирает аргументы командной строки."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--annotation", required=True, help="csv-аннотация из лабы 2"
    )
    parser.add_argument(
        "--output_csv", default="dominant_colors.csv",
        help="файл для сохранения DataFrame",
    )
    parser.add_argument(
        "--output_plot", default="dominant_colors_hist.png",
        help="файл для сохранения гистограммы",
    )
    parser.add_argument(
        "--descending", action="store_true",
        help="сортировать по убыванию (по умолчанию по возрастанию)",
    )
    parser.add_argument(
        "--filter_color", choices=CHANNELS,
        help="вывести изображения только с этим доминирующим цветом",
    )
    return parser.parse_args()


def main() -> None:
    """Формирует DataFrame, сортирует, фильтрует, строит график и сохраняет."""
    args = parse_args()
    try:
        df = add_dominant_color(load_annotation(args.annotation))
        df = sort_by_dominant_color(df, ascending=not args.descending)
        if args.filter_color:
            filtered = filter_by_dominant_color(df, args.filter_color)
            print(f"Изображения с доминирующим цветом '{args.filter_color}':")
            print(filtered)
        df.to_csv(args.output_csv, index=False)
        plot_dominant_color_histogram(df, args.output_plot)
    except (OSError, ValueError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()