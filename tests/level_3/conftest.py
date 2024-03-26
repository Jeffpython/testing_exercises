import pytest
import datetime
import decimal
from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory


@pytest.fixture()
def make_expense():
    def expense(
            amount: float = 1,
            currency: Currency = Currency.RUB,
            spent_at: datetime = datetime.datetime(2024, 3, 10),
            spent_in: str = 'spent_in'
            # category: ExpenseCategory = ExpenseCategory.SUPERMARKET
    ):
        return Expense(
            amount=decimal.Decimal(amount),
            currency=currency,
            card=BankCard(last_digits='1234', owner='owner'),
            spent_in=spent_in,
            spent_at=spent_at,
            # category=category
            category=ExpenseCategory.SUPERMARKET
        )

    return expense
