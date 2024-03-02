import pytest

from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__discriminant_greater_than_zero():
    assert solve_square_equation(1, 2, -3) == (-3.0, 1.0)


@pytest.mark.xfail(reason="there must be one root")
def test__solve_square_equation__discriminant_equal_zero():
    assert solve_square_equation(1, -6, 9) == (3.0, None)


def test__solve_square_equation__discriminant_less_than_zero():
    assert solve_square_equation(1, 2, 2) == (None, None)


def test__solve_square_equation__square_coefficient_equal_zero():
    assert solve_square_equation(0, 2, -3) == (1.5, None)


def test__solve_square_equation__square_coefficient_and_linear_coefficient_equal_zero():
    assert solve_square_equation(0, 0, -3) == (None, None)
