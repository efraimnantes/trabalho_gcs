import math
from javalang.jfloat import JFloat

def test_jfloat_constants():
    assert JFloat.MAX_VALUE == 3.4028235e38
    assert JFloat.MIN_VALUE == 1.4e-45
    assert JFloat.MIN_NORMAL == 1.17549435e-38
    assert JFloat.POSITIVE_INFINITY == float('inf')
    assert JFloat.NEGATIVE_INFINITY == float('-inf')
    assert math.isnan(JFloat.NaN)
    assert JFloat.SIZE == 32
    assert JFloat.BYTES == 4

def test_jfloat_instantiation_float():
    jf = JFloat(3.14)
    assert jf.value == 3.14

def test_jfloat_instantiation_string():
    jf = JFloat("2.71")
    assert jf.value == 2.71
