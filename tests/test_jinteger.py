from javalang.jinteger import JInteger


def test_jinteger_creation():
    value = JInteger(10)

    assert value.value == 10