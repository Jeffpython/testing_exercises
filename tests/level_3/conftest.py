import pytest
import datetime
import decimal
from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory
from typing import Any

NOT_SET: Any = '___'


@pytest.fixture
def make_expenses(make_expense):
    def inner(count: int, **kwargs) -> list[Expense]:
        return [make_expense(**kwargs) for _ in range(count)]

    return inner


@pytest.fixture
def make_expense(faker):
    def inner(
        amount: float = NOT_SET,
        currency: Currency = NOT_SET,
        spent_in: str = NOT_SET,
        spent_at: datetime.datetime = NOT_SET,
        category: ExpenseCategory = NOT_SET
    ) -> Expense:

        amount = faker.pyfloat(min_value=0.01, max_value=5000) if amount is NOT_SET else amount
        currency = faker.enum(Currency) if currency is NOT_SET else currency
        spent_in = faker.pystr() if spent_in is NOT_SET else spent_in
        spent_at = faker.date_between() if spent_at is NOT_SET else spent_at
        category = faker.enum(ExpenseCategory) if category is NOT_SET else category

        return Expense(
            amount=decimal.Decimal(str(amount)),
            currency=currency,
            card=BankCard(last_digits='1234', owner='owner'),
            spent_in=spent_in,
            spent_at=spent_at,
            category=category
        )

    return inner
