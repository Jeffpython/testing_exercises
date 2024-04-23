from functions.level_4.two_students import get_student_by_tg_nickname
from faker import Faker
import pytest

faker = Faker()

@pytest.mark.parametrize('count', [1, 2])
def test__get_student_by_tg_nickname__returns_student_with_the_specified_telegram_account(make_students, count, telegram_account):
    students = make_students(count=count, telegram_account=telegram_account)
    assert get_student_by_tg_nickname(telegram_account, students) == students[0]


def test__get_student_by_tg_nickname__returns_none_if_students_list_is_empty(telegram_account):
    assert get_student_by_tg_nickname(telegram_account, students=[]) is None


def test__get_student_by_tg_nickname__returns_none_if_telegram_username_is_empty(make_student):
    students = [make_student()]
    assert get_student_by_tg_nickname(telegram_username='', students=students) is None


def test__get_student_by_tg_nickname__returns_none_if_the_telegram_username_is_not_found(make_student, telegram_account):
    students = [make_student(telegram_account=telegram_account)]
    assert get_student_by_tg_nickname(telegram_username=faker.pystr(), students=students) is None


def test__get_student_by_tg_nickname__returns_none_if_telegram_username_is_not_in_the_students_list(make_student, telegram_account):
    students = [make_student(telegram_account=None)]
    assert get_student_by_tg_nickname(telegram_username=telegram_account, students=students) is None
