import pytest
from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger


@pytest.fixture()
def delimiters():
    return {" ", ",", ".", "-", "/", "\\"}


@pytest.fixture()
def trigger():
    return 'apple'


@pytest.mark.parametrize(('original_string', 'trigger', 'expected_result'), [
    ('apple', 'apple', True),
    ('APPLE', 'apple', True),
])
def test__is_string_contains_trigger__returns_true_if_strings_match(original_string, trigger, expected_result):
    assert is_string_contains_trigger(original_string, trigger) == expected_result


def test__is_string_contains_trigger__returns_false_if_original_string_is_blank():
    assert is_string_contains_trigger('', 'apple') is False


def test__is_string_contains_trigger__returns_true_when_checking_delimiters_before_trigger(delimiters, trigger):
    for delimiter in delimiters:
        assert is_string_contains_trigger(f'{delimiter}{trigger}', trigger)


def test__is_string_contains_trigger__returns_true_when_checking_delimiters_after_trigger(delimiters, trigger):
    for delimiter in delimiters:
        assert is_string_contains_trigger(f'{trigger}{delimiter}', trigger)


def test__is_string_contains_trigger__returns_true_when_checking_delimiters_before_and_after_trigger(delimiters, trigger):
    for delimiter_1 in delimiters:
        for delimiter_2 in delimiters:
            assert is_string_contains_trigger(f'{delimiter_1}{trigger}{delimiter_2}', trigger)


def test__guess_expense_category__returns_category_if_strings_match(make_expense):
    expense = make_expense(spent_in='green apple')
    assert guess_expense_category(expense) == ExpenseCategory.SUPERMARKET


def test__guess_expense_category__returns_none_if_strings_not_match(make_expense):
    expense = make_expense(spent_in='none')
    assert guess_expense_category(expense) is None


def test__guess_expense_category__returns_none_if_spentin_is_blank(make_expense):
    expense = make_expense(spent_in='')
    assert guess_expense_category(expense) is None
    