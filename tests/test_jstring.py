import pytest

from javalang.jstring import JString


def test_jstring_creation_empty_constructor():
    value = JString()

    assert value.value == ""
    assert isinstance(value.value, str)


def test_jstring_creation_with_string():
    value = JString("teste")

    assert value.value == "teste"


def test_jstring_creation_from_original_jstring():
    original = JString("teste")
    copy = JString(original)

    assert copy.value == "teste"
    assert copy is not original


def test_jstring_value_is_read_only():
    value = JString("teste")

    with pytest.raises(AttributeError):
        value.value = "alterado"