"""Модуль для разбора и фильтрации анкет."""

import re


def parse_profiles(txt: str) -> list[str]:
    """
    Разделение текста на отдельные анкеты

    param txt: исходный текст
    param return: список анкет
    """
    profiles = re.split(r"\n\s*\n", txt)
    return [profile.strip() for profile in profiles if profile.strip()]


def filter_profiles(profiles: list[str]) -> list[str]:
    """
    Отбор анкет, где фамилия оканчивается на «ов/а».

    param profiles: список анкет
    return: список подходящих анкет
    """
    pattern_surname = re.compile(r"^Фамилия:[ \t]*[А-ЯЁа-яё]+ова?[ \t]*$", re.MULTILINE)
    return [profile for profile in profiles if pattern_surname.search(profile)]
