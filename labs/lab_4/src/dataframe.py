import pandas as pd

from image_analysis import CHANNELS, dominant_color

ABS_PATH_COLUMN = "absolute_path"
REL_PATH_COLUMN = "relative_path"
DOMINANT_COLOR_COLUMN = "dominant_color"


def load_annotation(annotation_path: str) -> pd.DataFrame:
    """Загружает csv-аннотацию в DataFrame с именованными колонками.

    :param annotation_path: путь к csv-файлу аннотации
    :return: DataFrame с колонками absolute_path и relative_path
    """
    df = pd.read_csv(annotation_path)
    if df.shape[1] < 2:
        raise ValueError("В аннотации должно быть минимум 2 колонки с путями")
    df = df.iloc[:, :2].copy()
    df.columns = [ABS_PATH_COLUMN, REL_PATH_COLUMN]
    return df


def _safe_dominant_color(image_path: str) -> str | None:
    """
    Возвращает доминирующий цвет или None, если файл не прочитался.
    
    :param image_path: путь к картинке
    :return: название цвета/ничего пр ошибке
    """
    try:
        return dominant_color(image_path)
    except FileNotFoundError as error:
        print(error)
        return None


def add_dominant_color(df: pd.DataFrame) -> pd.DataFrame:
    """Добавляет колонку с доминирующим цветом изображения.

    :param df: наша табличка (DataFrame)
    :return: новый DataFrame с колонкой dominant_color
    """
    result = df.copy()
    result[DOMINANT_COLOR_COLUMN] = result[ABS_PATH_COLUMN].apply(
        _safe_dominant_color
    )
    return result.dropna(subset=[DOMINANT_COLOR_COLUMN]).reset_index(drop=True)


def sort_by_dominant_color(
    df: pd.DataFrame, ascending: bool) -> pd.DataFrame:
    """Сортирует DataFrame по колонке доминирующего цвета.

    :param df: исходный DataFrame
    :param ascending: True - по возрастанию (b, g, r), False - по убыванию
    :return: отсортированный DataFrame
    """
    return df.sort_values(
        by=DOMINANT_COLOR_COLUMN, ascending=ascending, kind="stable"
    ).reset_index(drop=True)


def filter_by_dominant_color(df: pd.DataFrame, color: str) -> pd.DataFrame:
    """Оставляет только изображения с заданным доминирующим цветом.

    :param df: исходный DataFrame (табличка)
    :param color: цветик
    :return: отфильтрованный DataFrame
    """
    if color not in CHANNELS:
        raise ValueError(f"Цвет должен быть одним из {CHANNELS}, получено: {color}")
    return df[df[DOMINANT_COLOR_COLUMN] == color].reset_index(drop=True)