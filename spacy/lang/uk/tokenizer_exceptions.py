# encoding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, NORM


_exc = {}

_abbrev_exc = [
    # Weekdays abbreviations
    {ORTH: "пн", LEMMA: "понеділок", NORM: "понеділок"},
    {ORTH: "вт", LEMMA: "вівторок", NORM: "вівторок"},
    {ORTH: "ср", LEMMA: "середа", NORM: "середа"},
    {ORTH: "чт", LEMMA: "четвер", NORM: "четвер"},
    {ORTH: "чтв", LEMMA: "четвер", NORM: "четвер"},
    {ORTH: "пт", LEMMA: "п'ятниця", NORM: "п'ятниця"},
    {ORTH: "сб", LEMMA: "субота", NORM: "субота"},
    {ORTH: "сбт", LEMMA: "субота", NORM: "субота"},
    {ORTH: "нд", LEMMA: "неділя", NORM: "неділя"},
    {ORTH: "ндл", LEMMA: "неділя", NORM: "неділя"},
    
    # Months abbreviations
    {ORTH: "січ", LEMMA: "січень", NORM: "січень"},
    {ORTH: "лют", LEMMA: "лютий", NORM: "лютий"},
    {ORTH: "бер", LEMMA: "березень", NORM: "березень"},
    {ORTH: "кві", LEMMA: "квітень", NORM: "квітень"},
    {ORTH: "тра", LEMMA: "травень", NORM: "травень"},
    {ORTH: "чер", LEMMA: "червень", NORM: "червень"},
    {ORTH: "лип", LEMMA: "липень", NORM: "липень"},
    {ORTH: "сер", LEMMA: "серпень", NORM: "серпень"},
    {ORTH: "вер", LEMMA: "вересень", NORM: "вересень"},
    {ORTH: "жов", LEMMA: "жовтень", NORM: "жовтень"},
    {ORTH: "лис", LEMMA: "листопад", NORM: "листопад"},
    {ORTH: "гру", LEMMA: "грудень", NORM: "грудень"},
]


for abbrev_desc in _abbrev_exc:
    abbrev = abbrev_desc[ORTH]
    for orth in (abbrev, abbrev.capitalize(), abbrev.upper()):
        _exc[orth] = [{ORTH: orth, LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}]
        _exc[orth + '.'] = [{ORTH: orth + '.', LEMMA: abbrev_desc[LEMMA], NORM: abbrev_desc[NORM]}]


_slang_exc = [
    {ORTH: '2к15', LEMMA: '2015', NORM: '2015'},
    {ORTH: '2к16', LEMMA: '2016', NORM: '2016'},
    {ORTH: '2к17', LEMMA: '2017', NORM: '2017'},
    {ORTH: '2к18', LEMMA: '2018', NORM: '2018'},
    {ORTH: '2к19', LEMMA: '2019', NORM: '2019'},
    {ORTH: '2к20', LEMMA: '2020', NORM: '2020'},
]

for slang_desc in _slang_exc:
    _exc[slang_desc[ORTH]] = [slang_desc]


TOKENIZER_EXCEPTIONS = _exc
