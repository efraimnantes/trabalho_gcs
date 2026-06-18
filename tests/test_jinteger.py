import pytest
from javalang.jinteger import JInteger

def test_jinteger_constants():
    # Valida as constantes exigidas pelos critérios de aceite
    assert JInteger.MAX_VALUE == 2147483647
    assert JInteger.MIN_VALUE == -2147483648
    assert JInteger.SIZE == 32
    assert JInteger.BYTES == 4
    assert JInteger.TYPE == int

def test_jinteger_creation_with_int():
    obj = JInteger(100)
    assert obj.value == 100

def test_jinteger_creation_with_numeric_string():
    obj = JInteger("42")
    assert obj.value == 42

def test_jinteger_creation_with_invalid_string():
    with pytest.raises(ValueError):
        JInteger("abc")