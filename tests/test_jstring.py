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


def test_jstring_length_and_is_empty():
    js_vazia = JString("")
    js_texto = JString("JavaLang")

    assert js_vazia.length() == 0
    assert js_vazia.isEmpty() is True

    assert js_texto.length() == 8
    assert js_texto.isEmpty() is False


def test_jstring_char_at_valid():
    js = JString("Python")

    assert js.charAt(0) == "P"
    assert js.charAt(5) == "n"


def test_jstring_char_at_invalid():
    js = JString("GCS")

    with pytest.raises(IndexError):
        js.charAt(-1)

    with pytest.raises(IndexError):
        js.charAt(3)

def test_jstring_comparison():
    js1 = JString("Java")
    js2 = JString("Java")
    js3 = JString("java")
    js4 = JString("Python")
    
    # Testando equals()
    assert js1.equals(js2) is True
    assert js1.equals(js3) is False
    assert js1.equals("Java") is True
    assert js1.equals(js4) is False
    
    # Testando equalsIgnoreCase()
    assert js1.equalsIgnoreCase(js3) is True
    assert js1.equalsIgnoreCase("JAVA") is True
    assert js1.equalsIgnoreCase(js4) is False
    
    # Testando hashCode / __hash__
    assert hash(js1) == hash(js2)
