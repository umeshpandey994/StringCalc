import pytest
from operations.calculator import Calculator


def test_add_empty_string():
    calc = Calculator()
    assert calc.calculate("") == 0


def test_add_with_default_delimiter():
    calc = Calculator()
    assert calc.calculate("1,2", "add") == 3


def test_add_with_custom_single_delimiter():
    calc = Calculator()
    assert calc.calculate("1;2", delimiter=[";"]) == 3


def test_add_with_custom_multiple_delimiters():
    calc = Calculator()
    assert calc.calculate("1;2&3", delimiter=[";", "&"]) == 6


def test_add_with_multiple_delimiter():
    calc = Calculator()
    assert calc.calculate("1\n2, 3", delimiter=["\n", ","]) == 6


def test_add_with_multiple_delimiter_v1():
    calc = Calculator()
    assert calc.calculate("//;\n1;2", delimiter=["\n", ";", "//"]) == 3


def test_negative_numbers_not_allowed():
    calc = Calculator()
    assert calc.calculate("1,-2,3") == "Negative numbers not allowed: [-2]"

