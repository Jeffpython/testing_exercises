import pytest

from functions.level_1.two_date_parser import compose_datetime_from
import datetime


@pytest.fixture
def today():
    return datetime.date.today()


@pytest.fixture
def tomorrow(today):
    return today + datetime.timedelta(days=1)


def test_compose_datetime_from__tomorrow(tomorrow):
    assert compose_datetime_from('tomorrow', '0:0').date() == tomorrow


def test_compose_datetime_from__blank_date(today):
    tomorrow = today + datetime.timedelta(days=1)

    assert compose_datetime_from('', '0:0').date() == today
