import pytest
from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(('text', 'replace_from', 'replace_to', 'expected_result'), [
    ('old old', 'old', 'new', 'new new'),
    ('OLD OLD', 'old', 'new', 'new new'),
    ('old', 'old', '', ''),
])
def test__replace_word__replace_all_words(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(('text', 'replace_from', 'replace_to', 'expected_result'), [
    ('old', 'other', 'new', 'old'),
    ('', 'old', 'new', ''),
    ('old', '', 'new', 'old'),
])
def test__replace_word__do_not_replace_words(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result
