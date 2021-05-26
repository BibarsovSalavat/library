#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------- #
# Patronymic
# Версия: 0.1 (Beta)
# Лицензия: GPL-3+
# Дата: 26.05.2021
# Автор: Салават Бибарсов
# E-Mail: <Bibarsov.Salavat@gmail.com>
# Описание: Класс Patronymic преобразует имена в отчества по правилам русского языка
# ------------------------------------------------------------------------------------------------------------------- #
# http://zags.kurganobl.ru/obrazovanie_i_napisanie_otchestv.html - Описание правил образования отчеств.               #

__all__ = ['Patronymic', ]

_ENDS_PATRONYMIC = ['ов', 'ев', 'ьев', 'ич']
_SHIFTS = [None, -1, -2]
_EXCEPTIONS = ('аникита', 'никита', 'мина', 'савва', 'сила', 'фока', 'фома')
_ENDS_NAME = [
    ['нтий', 'бий', 'вий', 'гий', 'дий', 'жий', 'зий', 'йий', 'лий', 'мий', 'ний', 'пий', 'рий', 'сий', 'тий', 'фий',
     'чий', 'ший', 'щий', ],
    ['бь', 'вь', 'гь', 'дь', 'жь', 'зь', 'йь', 'кь', 'ль', 'мь', 'нь', 'пь', 'рь', 'сь', 'ть', 'фь', 'хь', 'ць', 'чь',
     'шь', 'щь', ],
    ['жа', 'жу', 'жи', 'ша', 'шу', 'ши', 'ча', 'чу', 'чы', 'чи', 'ща', 'щу', 'щы', 'щи', 'ца', 'цу', 'цы', 'ци', ],
    ['ай', 'яй', 'ей', 'ёй', 'эй', 'ый', 'ой', 'уй', 'юй', ],
    ['аа', 'ау', 'еу', 'ээ', 'ии', 'оо', 'уу', ],
    ['ея', 'ия', ],
    ['ий', ],
    ['б', 'в', 'г', 'д', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', ],
    ['а', 'я', 'е', 'э', 'и', 'ы', 'ё', 'о', 'у', 'ю', ],
    ['ж', 'ш', 'ч', 'щ', 'ц', ],
    ['А', 'У', 'Ы', ],
    ['Е', ],
    ['И', ],
    ['О', ],
    ]


def _exceptions_exist(name: str) -> bool:

    if name.lower() in _EXCEPTIONS:
        return True


def _find_rule(name: str) -> int:

    for index, rule in enumerate(_ENDS_NAME):
        for end in rule:
            if name.endswith(end):
                return index


def _find_shift(rule_index: int) -> int:

    if rule_index in [4, 7, 8, 9, 12, ]:
        return 0
    elif rule_index in [1, 2, 3, 5, 6, 10, 11, 13, ]:
        return 1
    elif rule_index in [0, ]:
        return 2


def _find_end(rule_index: int) -> int:

    if rule_index in [7, 10, ]:
        return 0
    elif rule_index in [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, ]:
        return 1
    elif rule_index in [0, 13]:
        return 2


class Patronymic:

    def __init__(self, name: str):

        self.name = name

        if not _exceptions_exist(name):
            rule = _find_rule(name)

            shift = _find_shift(rule)
            suffix = _find_end(rule)

            cut = _SHIFTS[shift]
            end = _ENDS_PATRONYMIC[suffix]
            genders = {'male': end + 'ич', 'female': end + 'на'}

        else:
            cut = _SHIFTS[1]
            end = _ENDS_PATRONYMIC[3]
            genders = {'male': end, 'female': end + 'на'}

        self.male = name[0:cut] + genders['male']
        self.female = name[0:cut] + genders['female']


test = Patronymic('Салават')
print(test.female)
