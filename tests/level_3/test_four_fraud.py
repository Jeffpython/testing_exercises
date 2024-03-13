
from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__returns_len_fraud_transactions_greater_than_zero_if_amount_less_than_5000_and_transactions_amount_equal_3(make_expense):
    history = [
        make_expense(amount=4999),
        make_expense(amount=4999),
        make_expense(amount=4999),
    ]

    assert len(find_fraud_expenses(history)) > 0


def test__find_fraud_expenses__returns_len_fraud_transactions_greater_than_zero_if_amount_equal_5000_and_transactions_amount_equal_3(make_expense):
    history = [
        make_expense(amount=5000),
        make_expense(amount=5000),
        make_expense(amount=5000),
    ]

    assert len(find_fraud_expenses(history)) > 0


def test__find_fraud_expenses__returns_len_fraud_transactions_equal_zero_if_amount_great_than_5000_and_transactions_amount_equal_3(make_expense):
    history = [
        make_expense(amount=5001),
        make_expense(amount=5001),
        make_expense(amount=5001),
    ]

    assert len(find_fraud_expenses(history)) == 0


def test__find_fraud_expenses__returns_len_fraud_transactions_equal_zero_if_amount_great_than_5000_and_transactions_amount_less_than_3(make_expense):
    history = [
        make_expense(amount=1),
        make_expense(amount=1),
    ]

    assert len(find_fraud_expenses(history)) == 0


def test__find_fraud_expenses__returns_len_fraud_transactions_greater_than_zero_if_amount_great_than_5000_and_transactions_amount_greater_than_3(make_expense):
    history = [
        make_expense(amount=1),
        make_expense(amount=1),
        make_expense(amount=1),
        make_expense(amount=1),
    ]

    assert len(find_fraud_expenses(history)) > 0