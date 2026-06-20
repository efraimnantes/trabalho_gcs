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


def test_parse_int_with_radix():
    assert JInteger.parseInt("1010", 2) == 10
    assert JInteger.parseInt("12", 8) == 10
    assert JInteger.parseInt("10", 10) == 10
    assert JInteger.parseInt("A", 16) == 10
    assert JInteger.parseInt("-FF", 16) == -255


def test_parse_int_invalid_radix():
    with pytest.raises(ValueError):
        JInteger.parseInt("10", 1)

    with pytest.raises(ValueError):
        JInteger.parseInt("10", 37)


def test_value_of_with_radix():
    obj = JInteger.valueOf("1010", 2)
    assert isinstance(obj, JInteger)
    assert obj.value == 10


def test_decode_valid_prefixes():
    assert JInteger.decode("0x10").value == 16
    assert JInteger.decode("-0X10").value == -16
    assert JInteger.decode("#10").value == 16
    assert JInteger.decode("010").value == 8
    assert JInteger.decode("-010").value == -8
    assert JInteger.decode("10").value == 10
    assert JInteger.decode("+10").value == 10


def test_decode_invalid_strings():
    with pytest.raises(ValueError):
        JInteger.decode("")

    with pytest.raises(ValueError):
        JInteger.decode("-")

    with pytest.raises(ValueError):
        JInteger.decode("0xG")