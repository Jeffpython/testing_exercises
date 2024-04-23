from functions.level_4.two_students import Student
from faker import Faker
import pytest

faker = Faker()

NOT_SET = '___'


@pytest.fixture
def create_students(create_student):
    def inner(count: int, **kwargs) -> list[Student]:
        return [create_student(**kwargs) for _ in range(count)]

    return inner


@pytest.fixture
def create_student(faker):
    def inner(
        first_name: str = NOT_SET,
        last_name: str = NOT_SET,
        telegram_account: str | None = NOT_SET
    ) -> Student:

        return Student(
            faker.first_name() if first_name == NOT_SET else first_name,
            faker.last_name() if last_name == NOT_SET else last_name,
            faker.pystr() if telegram_account == NOT_SET else telegram_account
        )

    return inner


@pytest.fixture
def create_file(tmp_path):
    def inner(content, format='txt'):
        d = tmp_path / 'test'
        d.mkdir()
        p = d / f'test.{format}'
        p.write_text(content)
        return str(p)

    return inner
