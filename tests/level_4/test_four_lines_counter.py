from unittest.mock import patch

import pytest

from functions.level_4.four_lines_counter import count_lines_in


@patch('functions.level_4.four_lines_counter.os.path.isfile')
def test__count_lines_in__returns_none_if_the_file_does_not_exist(isfile_mock):
    isfile_mock.return_value = False
    assert count_lines_in('') is None


@pytest.mark.parametrize(('content', 'expected'), [
    ('', 0),
    ('1', 1),
    ('1\n2', 2)
])
def test__count_lines_in__returns_number_of_lines(make_file, content, expected):
    filepath = make_file(content=content)
    assert count_lines_in(filepath) == expected


@pytest.mark.parametrize('content', ['#', ' #'])
def test__count_lines_in__line_is_not_counted_if_it_starts_with_number_sign(make_file, content):
    filepath = make_file(content=content)
    assert count_lines_in(filepath) == 0
