import datetime
from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__is_not_subscription_if_same_destination_expenses_lh_three(make_expense, make_expenses):
    expense = make_expense(spent_in='Магнит')
    history = make_expenses(count=2, spent_in='Магнит')
    assert is_subscription(expense, history) is False


def test__is_subscription__is_not_subscription_if_expenses_amount_for_month_gh_one(make_expense, make_expenses):
    expense = make_expense(spent_in='Магнит')
    history = make_expenses(count=2, spent_in='Магнит',  spent_at=datetime.datetime(2024,1,10))
    assert is_subscription(expense, history) is False

def test__is_subscription__is_subscription_if_same_destination_expenses_equals_three_and_month_to_expenses_amount_equal_one(make_expense):
    expense = make_expense(spent_in='Магнит')
    history = [
        make_expense(spent_in='Магнит', spent_at=datetime.datetime(2024,1,10)),
        make_expense(spent_in='Магнит', spent_at=datetime.datetime(2024,2,10)),
        make_expense(spent_in='Магнит', spent_at=datetime.datetime(2024,3,10)),
    ]

    assert is_subscription(expense, history)


def test__is_subscription__is_subscription_if_same_destination_expenses_gh_three_and_month_to_expenses_amount_equal_one(make_expense):
    expense = make_expense(spent_in='Магнит')
    history = [
        make_expense(spent_in='Магнит', spent_at=datetime.datetime(2024,1,10)),
        make_expense(spent_in='Магнит', spent_at=datetime.datetime(2024,2,10)),
        make_expense(spent_in='Магнит', spent_at=datetime.datetime(2024,3,10)),
        make_expense(spent_in='Магнит', spent_at=datetime.datetime(2024,4,10)),
    ]

    assert is_subscription(expense, history)
