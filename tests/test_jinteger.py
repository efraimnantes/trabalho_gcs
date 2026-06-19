import pytest

from javalang.jinteger import JInteger
def test_jinteger_creation():
    value = JInteger(10)
    assert value.value == 10


def test_jinteger_to_string():
    value = JInteger(10)
    assert value.toString() == "10"


def test_jinteger_equals():
    assert JInteger(10).equals(JInteger(10)) is True
    assert JInteger(10).equals(JInteger(20)) is False
    assert JInteger(10).equals(10) is False


def test_jinteger_compare_to():
    assert JInteger(10).compareTo(JInteger(20)) == -1
    assert JInteger(20).compareTo(JInteger(20)) == 0
    assert JInteger(30).compareTo(JInteger(20)) == 1


def test_jinteger_compare_to_invalid_type():
    with pytest.raises(TypeError):
        JInteger(10).compareTo(10)