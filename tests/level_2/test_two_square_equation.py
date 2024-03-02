import pytest

from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__discriminant_greater_than_zero():
    square_coefficient = 1
    linear_coefficient = 2
    const_coefficient = -3

    expected_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert expected_result == (-3.0, 1.0)


@pytest.mark.xfail(reason="there must be one root")
def test__solve_square_equation__discriminant_equal_zero():
    square_coefficient = 1
    linear_coefficient = -6
    const_coefficient = 9

    expected_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert expected_result == (3.0, None)


def test__solve_square_equation__discriminant_less_than_zero():
    square_coefficient = 1
    linear_coefficient = 2
    const_coefficient = 2

    expected_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert expected_result == (None, None)


def test__solve_square_equation__square_coefficient_equal_zero():
    square_coefficient = 0
    linear_coefficient = 2
    const_coefficient = -3

    expected_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert expected_result == (1.5, None)


def test__solve_square_equation__square_coefficient_and_linear_coefficient_equal_zero():
    square_coefficient = 0
    linear_coefficient = 0
    const_coefficient = -3

    expected_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert expected_result == (None, None)
