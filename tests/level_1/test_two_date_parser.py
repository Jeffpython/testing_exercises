from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test_compose_datetime_from():
    today = datetime.date.today()

    assert compose_datetime_from('tomorrow', '0:0') == datetime.datetime(
        today.year,
        today.month,
        today.day + 1
    )

    assert compose_datetime_from('', '0:0') == datetime.datetime(
        today.year,
        today.month,
        today.day
    )
