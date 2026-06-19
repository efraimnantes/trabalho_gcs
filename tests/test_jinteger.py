from javalang.jinteger import JInteger

def test_jinteger_creation():
    value = JInteger(10)
    assert value.value == 10

def test_complementary_conversions():
    jint = JInteger(42)
    assert jint.doubleValue() == 42.0
    
def test_byte_and_short_overflow():
    jint_overflow = JInteger(130)
    assert jint_overflow.byteValue() == -126
    
    jint_short_overflow = JInteger(32769)
    assert jint_short_overflow.shortValue() == -32767