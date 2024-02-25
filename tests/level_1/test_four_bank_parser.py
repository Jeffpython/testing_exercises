import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense
import datetime


@pytest.fixture
def sms():
    return SmsMessage('sum: 11 USD, 1234123412341234 19.02.24 22:23 spent_in authcode ',
                      'author',
                      datetime.datetime.now())


@pytest.fixture
def cards():
    return [BankCard('1234', 'owner_1'),
            BankCard('0456', 'owner_2')]


def test_parse_ineco_expense__get_amount(sms, cards):
    expense = parse_ineco_expense(sms, cards)
    assert expense.amount == 11


def test_parse_ineco_expense__get_card_last_digits(sms, cards):
    expense = parse_ineco_expense(sms, cards)
    assert expense.card.last_digits == '1234'


def test_parse_ineco_expense__get_card_owner(sms, cards):
    expense = parse_ineco_expense(sms, cards)
    assert expense.card.owner == 'owner_1'


def test_parse_ineco_expense__get_spent_in(sms, cards):
    expense = parse_ineco_expense(sms, cards)
    assert expense.spent_in == 'spent_in'


def test_parse_ineco_expense__get_spent_at(sms, cards):
    expense = parse_ineco_expense(sms, cards)
    assert expense.spent_at.strftime('%d.%m.%y %H:%M') == '19.02.24 22:23'
