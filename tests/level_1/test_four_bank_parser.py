from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal


def test_parse_ineco_expense():
    sms = SmsMessage('sum: 1234 USD, 1234123412341234 19.02.24 22:23 spend_in authcode ',
                     'author',
                     datetime.datetime.now())
    cards = [BankCard('1234', 'owner_1'),
             BankCard('0456', 'owner_2')]

    assert parse_ineco_expense(sms, cards) == Expense(amount=decimal.Decimal('1234'),
                                                      card=BankCard(last_digits='1234', owner='owner_1'),
                                                      spent_in='spend_in',
                                                      spent_at=datetime.datetime(2024, 2, 19, 22, 23))
