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

def test_jstring_substring():
    js = JString("JavaLang")
    
    # Teste recorte do início ao fim (apenas beginIndex)
    assert js.substring(4)._value == "Lang"
    
    # Teste recorte por intervalo (beginIndex e endIndex)
    assert js.substring(0, 4)._value == "Java"
    
    # Teste subSequence
    assert js.subSequence(0, 4)._value == "Java"

def test_jstring_substring_invalid_index():
    js = JString("Python")
    
    # Índices negativos ou fora do tamanho
    with pytest.raises(IndexError):
        js.substring(-1)
    with pytest.raises(IndexError):
        js.substring(0, 10)
        
    # endIndex menor que o beginIndex
    with pytest.raises(IndexError):
        js.substring(4, 2)

def test_jstring_concat():
    js = JString("Java")

    assert js.concat("Lang").value == "JavaLang"
    assert js.concat(JString("Script")).value == "JavaScript"


def test_jstring_replace():
    js1 = JString("banana")
    js2 = JString("hello world")

    assert js1.replace("a", "o").value == "bonono"
    assert js2.replace("world", "Python").value == "hello Python"
    assert js2.replace("Java", "C").value == "hello world"
