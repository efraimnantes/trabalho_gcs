from javalang.jstring import JString


def test_jstring_creation():
    value = JString("teste")

    assert value.value == "teste"