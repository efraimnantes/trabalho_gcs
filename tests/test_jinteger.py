import pytest

from javalang.jinteger import JInteger


def test_jinteger_constants():
    # Valida as constantes exigidas pelos critérios de aceite
    assert JInteger.MAX_VALUE == 2147483647
    assert JInteger.MIN_VALUE == -2147483648
    assert JInteger.SIZE == 32
    assert JInteger.BYTES == 4
    assert JInteger.TYPE is int


def test_jinteger_creation_with_int():
    obj = JInteger(100)
    assert obj.value == 100


def test_jinteger_creation_with_numeric_string():
    obj = JInteger("42")
    assert obj.value == 42


def test_jinteger_creation_with_invalid_string():
    with pytest.raises(ValueError):
        JInteger("abc")


def test_parse_int_valid_string():
    result = JInteger.parseInt("123")
    assert result == 123
    assert isinstance(result, int)


def test_parse_int_invalid_string():
    with pytest.raises(ValueError):
        JInteger.parseInt("abc")

    with pytest.raises(ValueError):
        JInteger.parseInt("12.34")


def test_value_of_with_int():
    obj = JInteger.valueOf(500)
    assert isinstance(obj, JInteger)
    assert obj.value == 500


def test_value_of_with_valid_string():
    obj = JInteger.valueOf("999")
    assert isinstance(obj, JInteger)
    assert obj.value == 999


def test_value_of_with_invalid_string():
    with pytest.raises(ValueError):
        JInteger.valueOf("xyz")
