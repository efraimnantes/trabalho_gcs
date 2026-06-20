from javalang.jinteger import JInteger

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
