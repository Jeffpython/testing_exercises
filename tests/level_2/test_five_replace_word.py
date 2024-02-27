import pytest
from functions.level_2.five_replace_word import replace_word


def test__replace_word__one_word_from_text_contains_in_replace_word():
    text = 'old'
    replace_from = 'old'
    replace_to = 'new'

    expected_result = replace_word(text, replace_from, replace_to)
    assert expected_result == 'new'


def test__replace_word__two_words_from_text_contains_in_replace_word():
    text = 'old old'
    replace_from = 'old'
    replace_to = 'new'

    expected_result = replace_word(text, replace_from, replace_to)
    assert expected_result == 'new new'


def test__replace_word__upper_word_from_text_contains_in_replace_word():
    text = 'OLD OLD'
    replace_from = 'old'
    replace_to = 'new'

    expected_result = replace_word(text, replace_from, replace_to)
    assert expected_result == 'new new'


def test__replace_word__word_from_text_not_contains_in_replace_word():
    text = 'old'
    replace_from = 'other'
    replace_to = 'new'

    expected_result = replace_word(text, replace_from, replace_to)
    assert expected_result == 'old'


def test__replace_word__text_is_blank():
    text = ''
    replace_from = 'old'
    replace_to = 'new'

    expected_result = replace_word(text, replace_from, replace_to)
    assert expected_result == ''


def test__replace_word__replace_from_is_blank():
    text = 'old'
    replace_from = ''
    replace_to = 'new'

    expected_result = replace_word(text, replace_from, replace_to)
    assert expected_result == 'old'


def test__replace_word__replace_to_is_blank():
    text = 'old'
    replace_from = 'old'
    replace_to = ''

    expected_result = replace_word(text, replace_from, replace_to)
    assert expected_result == ''
