import pytest
import datetime

from functions.level_3.four_fraud import find_fraud_expenses


@pytest.mark.parametrize('count', [3, 4])
def test__find_fraud_expenses__detect_fraud_if_count_of_transactions_ge_three(make_expenses, count):
    history = make_expenses(
        count=count,
        spent_in='Магнит',
        spent_at=datetime.datetime(2024, 3, 10),
        amount=5000
    )

    assert len(find_fraud_expenses(history)) > 0


def test__find_fraud_expenses__no_fraud_detected_is_not_fraud_if_count_of_transactions_lt_three(make_expenses):
    history = make_expenses(
        count=2,
        spent_in='Магнит',
        spent_at=datetime.datetime(2024, 3, 10),
        amount=5000
    )

    assert len(find_fraud_expenses(history)) == 0


def test__find_fraud_expenses__no_fraud_detected_if_amount_transactions_gt_large_amount(make_expenses):
    history = make_expenses(
        count=3,
        spent_in='Магнит',
        spent_at=datetime.datetime(2024, 3, 10),
        amount=5001
    )

    assert len(find_fraud_expenses(history)) == 0


@pytest.mark.parametrize('amount', [4999, 5000])
def test__find_fraud_expenses__detect_fraud_if_amount_transactions_le_large_amount(make_expenses, amount):
    history = make_expenses(
        count=3,
        spent_in='Магнит',
        spent_at=datetime.datetime(2024, 3, 10),
        amount=amount
    )

    assert len(find_fraud_expenses(history)) > 0


def test__find_fraud_expenses__no_fraud_detected_if_place_of_transactions_is_different(make_expense):
    history = [
        make_expense(spent_in='Магнит',
                     spent_at=datetime.datetime(2024, 3, 10),
                     amount=5000),
        make_expense(spent_in='Пятерочка',
                     spent_at=datetime.datetime(2024, 3, 10),
                     amount=5000),
        make_expense(spent_in='Перекресток',
                     spent_at=datetime.datetime(2024, 3, 10),
                     amount=5000)
    ]

    assert len(find_fraud_expenses(history)) == 0


def test__find_fraud_expenses__no_fraud_detected_if_transactions_is_not_simultaneous(make_expense):
    history = [
        make_expense(spent_in='Магнит',
                     spent_at=datetime.datetime(2024, 3, 10),
                     amount=5000),
        make_expense(spent_in='Магнит',
                     spent_at=datetime.datetime(2024, 3, 11),
                     amount=5000),
        make_expense(spent_in='Магнит',
                     spent_at=datetime.datetime(2024, 3, 12),
                     amount=5000)
    ]

    assert len(find_fraud_expenses(history)) == 0


def test__find_fraud_expenses__no_fraud_detected_if_amount_of_transactions_is_different(make_expense):
    history = [
        make_expense(spent_in='Магнит',
                     spent_at=datetime.datetime(2024, 3, 10),
                     amount=1000),
        make_expense(spent_in='Магнит',
                     spent_at=datetime.datetime(2024, 3, 10),
                     amount=2000),
        make_expense(spent_in='Магнит',
                     spent_at=datetime.datetime(2024, 3, 10),
                     amount=3000)
    ]

    assert len(find_fraud_expenses(history)) == 0


def test__find_fraud_expenses__no_transactions():
    assert len(find_fraud_expenses(history=[])) == 0
