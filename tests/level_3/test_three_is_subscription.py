import datetime
from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__returns_false_if_same_destination_expenses_less_than_3(make_expense):
    expense = make_expense()
    history = [
        make_expense(spent_at=datetime.datetime(2024,1,10)),
        make_expense(spent_at=datetime.datetime(2024,1,10)),
    ]

    assert is_subscription(expense, history) is False


def test__is_subscription__returns_false_if_month_to_expenses_amount_greater_than_1(make_expense):
    expense = make_expense()
    history = [
        make_expense(spent_at=datetime.datetime(2024,1,10)),
        make_expense(spent_at=datetime.datetime(2024,1,10)),
    ]

    assert is_subscription(expense, history) is False


def test__is_subscription__returns_true_if_same_destination_expenses_equals_3_and_month_to_expenses_amount_equal_1(make_expense):
    expense = make_expense()
    history = [
        make_expense(spent_at=datetime.datetime(2024,1,10)),
        make_expense(spent_at=datetime.datetime(2024,2,10)),
        make_expense(spent_at=datetime.datetime(2024,3,10)),
    ]

    assert is_subscription(expense, history)


def test__is_subscription__returns_true_if_same_destination_expenses_greater_than_3_and_month_to_expenses_amount_equal_1(make_expense):
    expense = make_expense()
    history = [
        make_expense(spent_at=datetime.datetime(2024,1,10)),
        make_expense(spent_at=datetime.datetime(2024,2,10)),
        make_expense(spent_at=datetime.datetime(2024,3,10)),
        make_expense(spent_at=datetime.datetime(2024,4,10)),
    ]

    assert is_subscription(expense, history)
