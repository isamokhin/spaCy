# coding: utf-8
"""Test that tokenizer exceptions are parsed correctly."""


from __future__ import unicode_literals

import pytest


@pytest.mark.parametrize('text,norms', [("пн.", ["понеділок"]),
                                        ("пт.", ["п'ятниця"]),
                                        ("гру.", ["грудень"])])
def test_ru_tokenizer_abbrev_exceptions(uk_tokenizer, text, norms):
    tokens = uk_tokenizer(text)
    assert len(tokens) == 1
    assert [token.norm_ for token in tokens] == norms
