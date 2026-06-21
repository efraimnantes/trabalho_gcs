import math

import pytest

from javalang.jfloat import JFloat

def test_jfloat_constants():
    assert JFloat.MAX_VALUE == 3.4028235e38
    assert JFloat.MIN_VALUE == 1.4e-45
    assert JFloat.MIN_NORMAL == 1.17549435e-38
    assert JFloat.POSITIVE_INFINITY == float("inf")
    assert JFloat.NEGATIVE_INFINITY == float("-inf")
    assert math.isnan(JFloat.NaN)
    assert JFloat.SIZE == 32
    assert JFloat.BYTES == 4

def test_jfloat_constructor():
    obj = JFloat(3.14)
    assert obj.value == 3.14

    obj_str = JFloat("2.5")
    assert obj_str.value == 2.5

def test_parse_float_valid():
    result = JFloat.parseFloat("1.23")
    assert result == 1.23
    assert isinstance(result, float)

def test_parse_float_invalid():
    with pytest.raises(ValueError):
     JFloat.parseFloat("abc")
    with pytest.raises(ValueError):
     JFloat.parseFloat("")

def test_value_of_with_float():
    obj = JFloat.valueOf(5.5)
    assert isinstance(obj, JFloat)
    assert obj.value == 5.5

def test_value_of_with_string():
    obj = JFloat.valueOf("10.82")
    assert isinstance(obj, JFloat)
    assert obj.value == 10.82

def test_value_of_invalid_string():
    with pytest.raises(ValueError):
     JFloat.valueOf("invalid_float")

def test_jfloat_numeric_conversions_positive():
    jf = JFloat(120.75)
    assert jf.intValue() == 120
    assert jf.longValue() == 120
    assert jf.byteValue() == 120

def test_jfloat_numeric_conversions_negative():
    jf = JFloat(-45.3)
    assert jf.intValue() == -45
    assert jf.longValue() == -45
    assert jf.byteValue() == -45

def test_jfloat_byte_overflow():
    jf = JFloat(130.0)
    assert jf.byteValue() == -126

def test_float_value():
    obj = JFloat("3.14")
    assert obj.floatValue() == 3.14
    assert isinstance(obj.floatValue(), float)

def test_double_value():
    obj = JFloat(2.71828)
    assert obj.doubleValue() == 2.71828
    assert isinstance(obj.doubleValue(), float)

def test_to_string():
    obj = JFloat(10.5)
    assert obj.toString() == "10.5"
    assert isinstance(obj.toString(), str)

    obj_zero = JFloat(0.0)
    assert obj_zero.toString() == "0.0"

def test_jfloat_static_compare():
    assert JFloat.compare(1.0, 2.0) == -1
    assert JFloat.compare(2.0, 2.0) == 0
    assert JFloat.compare(3.5, 2.0) == 1

def test_jfloat_static_compare_with_negative_values():
    assert JFloat.compare(-5.0, -2.0) == -1
    assert JFloat.compare(-2.0, -5.0) == 1
    assert JFloat.compare(-3.0, -3.0) == 0

def test_jfloat_static_max():
    assert JFloat.max(1.0, 2.0) == 2.0
    assert JFloat.max(5.5, 2.5) == 5.5
    assert JFloat.max(-1.0, -3.0) == -1.0

def test_jfloat_static_min():
    assert JFloat.min(1.0, 2.0) == 1.0
    assert JFloat.min(5.5, 2.5) == 2.5
    assert JFloat.min(-1.0, -3.0) == -3.0

def test_jfloat_static_operations_with_zero_values():
    assert JFloat.compare(0.0, -0.0) == 0
    assert JFloat.max(0.0, -0.0) == 0.0
    assert JFloat.min(0.0, -0.0) == 0.0
