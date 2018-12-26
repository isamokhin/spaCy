# coding: utf8
from __future__ import unicode_literals


_exc = {
    # Slang
    'прив': 'привіт',
    'здоров': 'привіт',
    "да": "так",
    'ща': 'зараз',
    "зара": "зараз",
    'спс': 'дякую',
    'бдлск': 'будь ласка',
    'пліз': 'будь ласка',
    'ладненько': 'гаразд',
    'лан': 'гаразд',
    'ясн': 'ясно',
    'хоч': 'хочеш',
    'чо': 'що',
    'шо': 'що'
}


NORM_EXCEPTIONS = {}

for string, norm in _exc.items():
    NORM_EXCEPTIONS[string] = norm
    NORM_EXCEPTIONS[string.title()] = norm
