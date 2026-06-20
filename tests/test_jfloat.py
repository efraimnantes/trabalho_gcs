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