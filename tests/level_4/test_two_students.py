from functions.level_4.two_students import get_student_by_tg_nickname
import pytest


@pytest.mark.parametrize('count', [1, 2])
def test__get_student_by_tg_nickname__returns_student_with_the_specified_telegram_account(create_students, count):
    telegram_account = 'telegram_account'
    students = create_students(count=count, telegram_account=telegram_account)
    assert get_student_by_tg_nickname(telegram_account, students) == students[0]


def test__get_student_by_tg_nickname__returns_none_if_students_list_is_empty():
    assert get_student_by_tg_nickname('telegram_username', students=[]) is None


def test__get_student_by_tg_nickname__returns_none_if_telegram_username_is_empty(create_student):
    students = [create_student()]
    assert get_student_by_tg_nickname(telegram_username='', students=students) is None


def test__get_student_by_tg_nickname__returns_none_if_the_telegram_username_is_not_found(create_student):
    students = [create_student(telegram_account='telegram_username')]
    assert get_student_by_tg_nickname(telegram_username='other_telegram_username', students=students) is None


def test__get_student_by_tg_nickname__returns_none_if_telegram_username_is_not_in_the_students_list(create_student):
    students = [create_student(telegram_account=None)]
    assert get_student_by_tg_nickname(telegram_username='telegram_username', students=students) is None
