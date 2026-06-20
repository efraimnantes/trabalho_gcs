import pytest

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
  
  def test_jinteger_to_string():
  value = JInteger(10)
  assert value.toString() == "10"
  
  def test_jinteger_equals():
  assert JInteger(10).equals(JInteger(10)) is True
  assert JInteger(10).equals(JInteger(20)) is False
  assert JInteger(10).equals(10) is False
  
  def test_jinteger_compare_to():
  assert JInteger(10).compareTo(JInteger(20)) == -1
  assert JInteger(20).compareTo(JInteger(20)) == 0
  assert JInteger(30).compareTo(JInteger(20)) == 1
  
  def test_jinteger_compare_to_invalid_type():
  with pytest.raises(TypeError):
  JInteger(10).compareTo(10)
