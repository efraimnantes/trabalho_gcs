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

def test_jfloat_isnan():
    jf_nan = JFloat(float("nan"))
    jf_normal = JFloat(5.0)

    assert jf_nan.isNaN() is True
    assert jf_normal.isNaN() is False

def test_jfloat_isinfinite():
    jf_pos_inf = JFloat(float("inf"))
    jf_neg_inf = JFloat(float("-inf"))
    jf_normal = JFloat(10.5)

    assert jf_pos_inf.isInfinite() is True
    assert jf_neg_inf.isInfinite() is True
    assert jf_normal.isInfinite() is False

def test_jfloat_isfinite():
    assert JFloat.isFinite(10.5) is True
    assert JFloat.isFinite(float("inf")) is False
    assert JFloat.isFinite(float("nan")) is False