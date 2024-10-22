import pytest
from operations.calculator import Calculator


def test_mul_empty_string():
    calc = Calculator()
    assert calc.calculate("", "mul") == 0


def test_mul_with_default_delimiter():
    calc = Calculator()
    assert calc.calculate("1,2", "mul") == 2
