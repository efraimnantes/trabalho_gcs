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

    assert js1.equals(js2) is True
    assert js1.equals(js3) is False
    assert js1.equals("Java") is True
    assert js1.equals(js4) is False

    assert js1.equalsIgnoreCase(js3) is True
    assert js1.equalsIgnoreCase("JAVA") is True
    assert js1.equalsIgnoreCase(js4) is False

    assert hash(js1) == hash(js2)


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


def test_jstring_substring():
    js = JString("JavaLang")

    assert js.substring(4).value == "Lang"
    assert js.substring(0, 4).value == "Java"
    assert js.subSequence(0, 4).value == "Java"


def test_jstring_substring_invalid_index():
    js = JString("Python")

    with pytest.raises(IndexError):
        js.substring(-1)

    with pytest.raises(IndexError):
        js.substring(0, 10)

    with pytest.raises(IndexError):
        js.substring(4, 2)


def test_jstring_simple_search():
    js = JString("JavaLang")

    assert js.contains("Java") is True
    assert js.contains(JString("Lang")) is True
    assert js.contains("Python") is False

    assert js.startsWith("Java") is True
    assert js.startsWith(JString("Java")) is True
    assert js.startsWith("Lang") is False

    assert js.endsWith("Lang") is True
    assert js.endsWith(JString("Lang")) is True
    assert js.endsWith("Java") is False

def test_index_of_string():
    jstr = JString("hello world")

    assert jstr.indexOf("world") == 6
    assert jstr.indexOf("l") == 2
    assert jstr.indexOf("x") == -1


def test_index_of_string_with_from_index():
    jstr = JString("hello world")

    assert jstr.indexOf("l", 3) == 3
    assert jstr.indexOf("l", 4) == 9
    assert jstr.indexOf("world", 10) == -1


def test_index_of_int():
    jstr = JString("hello world")

    assert jstr.indexOf(111) == 4
    assert jstr.indexOf(111, 5) == 7
    assert jstr.indexOf(120) == -1


def test_last_index_of_string():
    jstr = JString("banana")

    assert jstr.lastIndexOf("a") == 5
    assert jstr.lastIndexOf("na") == 4
    assert jstr.lastIndexOf("x") == -1


def test_last_index_of_string_with_from_index():
    jstr = JString("banana")

    assert jstr.lastIndexOf("a", 4) == 3
    assert jstr.lastIndexOf("a", 2) == 1
    assert jstr.lastIndexOf("na", 3) == 2


def test_last_index_of_int():
    jstr = JString("banana")

    assert jstr.lastIndexOf(97) == 5
    assert jstr.lastIndexOf(97, 4) == 3
    assert jstr.lastIndexOf(120) == -1



# novos testes para toCharArray e getBytes

def test_to_char_array():
    jstr = JString("hello")
    chars = jstr.toCharArray()
    assert chars == ["h", "e", "l", "l", "o"]
    assert len(chars) == 5

def test_get_bytes_default():
    jstr = JString("java")
    b = jstr.getBytes()
    assert b == b"java"
    assert isinstance(b, bytes)

def test_get_bytes_with_charset():
    jstr = JString("ação")

    b_utf8 = jstr.getBytes("utf-8")
    assert b_utf8 == "ação".encode("utf-8")
    
    b_latin1 = jstr.getBytes("latin-1")
    assert b_latin1 == "ação".encode("latin-1")



# novos testes para regex 

def test_matches_full_string():
    jstr = JString("hello123world")
    assert jstr.matches("[a-z]+[0-9]+[a-z]+") is True
    
    assert jstr.matches("[0-9]+") is False

def test_replace_first_regex():
    jstr = JString("gato, cachorro, gato")

    result = jstr.replaceFirst("gato", "passarinho")
    assert result == "passarinho, cachorro, gato"

def test_replace_all_regex():
    jstr = JString("O ano é 2023, logo será 2024.")

    result = jstr.replaceAll("\\d+", "[DATA]")
    assert result == "O ano é [DATA], logo será [DATA]."



# novos testes para comparação ordenada

def test_compare_to():
    jstr = JString("banana")

    assert jstr.compareTo("banana") == 0
    assert jstr.compareTo("cebola") < 0
    assert jstr.compareTo("abacaxi") > 0

def test_compare_to_ignore_case():
    jstr = JString("Python")

    assert jstr.compareToIgnoreCase("PYTHON") == 0
    assert jstr.compareToIgnoreCase("python") == 0
    assert jstr.compareToIgnoreCase("Zebra") < 0
    assert jstr.compareToIgnoreCase("Abelha") > 0

def test_content_equals():
    jstr = JString("hello world")
    
    assert jstr.contentEquals("hello world") is True
    assert jstr.contentEquals("hello") is False