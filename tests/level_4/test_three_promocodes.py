from functions.level_4.three_promocodes import generate_promocode
from unittest.mock import patch


@patch('functions.level_4.three_promocodes.random.choice')
def test__generate_promocode__returns_promocode_if_length_is_not_specified(random_choice_mock):
    random_choice_mock.return_value = 'A'
    assert generate_promocode() == 'AAAAAAAA'


@patch('functions.level_4.three_promocodes.random.choice')
def test__generate_promocode__returns_string_of_the_specified_length(random_choice_mock):
    random_choice_mock.return_value = 'A'
    assert generate_promocode(1) == 'A'


def test__generate_promocode__returns_empty_string_if_zero_length_is_specified():
    assert generate_promocode(0) == ''
