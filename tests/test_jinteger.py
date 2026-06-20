from javalang.jinteger import JInteger


def test_jinteger_creation():
    value = JInteger(10)
    assert value.value == 10


def test_simple_conversions():
    jint = JInteger(42)
    assert jint.intValue() == 42
    assert jint.longValue() == 42
    assert jint.floatValue() == 42.0


def test_complementary_conversions():
    jint = JInteger(42)
    assert jint.doubleValue() == 42.0


def test_byte_and_short_overflow():
    jint_overflow = JInteger(130)
    assert jint_overflow.byteValue() == -126

    jint_short_overflow = JInteger(32769)
    assert jint_short_overflow.shortValue() == -32767


def test_compare():
    assert JInteger.compare(10, 20) == -1
    assert JInteger.compare(20, 20) == 0
    assert JInteger.compare(30, 20) == 1


def test_compare_unsigned():
    assert JInteger.compareUnsigned(-1, 1) == 1
    assert JInteger.compareUnsigned(1, -1) == -1
    assert JInteger.compareUnsigned(-1, -1) == 0
    assert JInteger.compareUnsigned(10, 20) == -1


def test_to_unsigned_string():
    assert JInteger.toUnsignedString(0) == "0"
    assert JInteger.toUnsignedString(123) == "123"
    assert JInteger.toUnsignedString(-1) == "4294967295"


def test_jinteger_double_value():
    value = JInteger(42)
    assert value.doubleValue() == 42.0


def test_jinteger_byte_value():
    assert JInteger(42).byteValue() == 42
    assert JInteger(130).byteValue() == -126
    assert JInteger(-1).byteValue() == -1


def test_jinteger_short_value():
    assert JInteger(42).shortValue() == 42
    assert JInteger(32769).shortValue() == -32767
    assert JInteger(-1).shortValue() == -1