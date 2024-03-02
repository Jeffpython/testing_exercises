import pytest
from functions.level_2.three_first import first


def test__first__items_with_one_element_without_default_return_first_element_of_list():
    items = [0]
    assert first(items) == 0


def test__first__blank_items_without_default_return_exception():
    items = []
    with pytest.raises(AttributeError):
        first(items)


def test__first__blank_items_with_default_return_default_value():
    items = []
    default = None
    assert first(items, default) is None


def test__first__number_in_items_without_default_return_exception():
    items = 1
    with pytest.raises(TypeError):
        first(items)
