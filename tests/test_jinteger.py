from javalang.jinteger import JInteger

def test_jinteger_creation():
    value = JInteger(10)
    assert value.value == 10

def test_simple_conversions():
    jint = JInteger(42)
    assert jint.intValue() == 42
    assert jint.longValue() == 42
    assert jint.floatValue() == 42.0