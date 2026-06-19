from javalang.jinteger import JInteger

def test_jinteger_creation():
    value = JInteger(10)
    assert value.value == 10

def test_jinteger_static_sum():
    assert JInteger.sum(2, 3) == 5
    assert JInteger.sum(-2, 3) == 1
    assert JInteger.sum(-2, -3) == -5
    assert JInteger.sum(0, 5) == 5


def test_jinteger_static_max():
    assert JInteger.max(10, 20) == 20
    assert JInteger.max(20, 10) == 20
    assert JInteger.max(-5, -2) == -2
    assert JInteger.max(0, -1) == 0


def test_jinteger_static_min():
    assert JInteger.min(10, 20) == 10
    assert JInteger.min(20, 10) == 10
    assert JInteger.min(-5, -2) == -5
    assert JInteger.min(0, -1) == -1