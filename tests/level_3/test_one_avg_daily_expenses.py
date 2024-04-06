import pytest
import datetime
import statistics
from functions.level_3.models import Currency
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


@pytest.mark.xfail(reason="different currencies should not be combined")
def test__calculate_average_daily_expenses__returns_average_of_expenses_for_different_currencies(make_expense):
    expense_in_rub = make_expense(amount=1, currency=Currency.RUB)
    expense_in_usd = make_expense(amount=1, currency=Currency.USD)
    assert calculate_average_daily_expenses([expense_in_rub, expense_in_usd]) == 2


def test__calculate_average_daily_expenses__returns_amount_of_expenses_for_one_day(make_expense):
    expense_1 = make_expense(amount=1, spent_at=datetime.datetime(2024,3,10))
    expense_2 = make_expense(amount=1, spent_at=datetime.datetime(2024,3,10))
    assert calculate_average_daily_expenses([expense_1, expense_2]) == 2


def test__calculate_average_daily_expenses__returns_average_of_expenses_in_different_days(make_expense):
    expense_1 = make_expense(amount=1, spent_at=datetime.datetime(2024,3,10))
    expense_2 = make_expense(amount=1, spent_at=datetime.datetime(2024,3,11))
    assert calculate_average_daily_expenses([expense_1, expense_2]) == 1


def test__calculate_average_daily_expenses__returns_exception_for_empty_expense(make_expense):
    with pytest.raises(statistics.StatisticsError):
        assert calculate_average_daily_expenses(expenses=[])
