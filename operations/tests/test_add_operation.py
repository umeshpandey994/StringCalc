import pytest
from operations.calculator import Calculator


def test_add_empty_string():
    calc = Calculator()
    assert calc.calculate("") == 0


def test_add_with_default_delimiter():
    calc = Calculator()
    assert calc.calculate("1,2", "add") == 3
