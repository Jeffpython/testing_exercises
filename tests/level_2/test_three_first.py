import pytest
from functions.level_2.three_first import first


def test__first__items_with_one_element_without_default_return_first_element_of_list():
    assert first([0]) == 0


def test__first__blank_items_without_default_return_exception():
    with pytest.raises(AttributeError):
        first([])


def test__first__blank_items_with_default_return_default_value():
    assert first([], None) is None
