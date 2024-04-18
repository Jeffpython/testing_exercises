import pytest
from functions.level_4.one_brackets import delete_remove_brackets_quotes


def test__delete_remove_brackets_quotes__returns_string_without_braces_if_string_starts_with_braces():
    assert delete_remove_brackets_quotes('{ s }') == 's'


@pytest.mark.parametrize(('string', 'expected'), [
    (' {s}', ' {s}'),
    (' ', ' ')
])
def test__delete_remove_brackets_quotes__returns_unchanged_string_if_string_not_starts_with_curly_braces(string, expected):
    assert delete_remove_brackets_quotes(string) == expected


def test__delete_remove_brackets_quotes__returns_exception_for_empty_string():
    with pytest.raises(IndexError):
        assert delete_remove_brackets_quotes('')


@pytest.mark.xfail(reason='only curly braces should be removed from a string')
def test__delete_remove_brackets_quotes__returns_exception_for_empty_string():
    assert delete_remove_brackets_quotes('{*') == ''
