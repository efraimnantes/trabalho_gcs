import pytest
from javalang.jstring import JString

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
