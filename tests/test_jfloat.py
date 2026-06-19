from javalang.jfloat import JFloat

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
    # Em Java, converter 130 para byte resulta em -126 devido ao estouro de 8 bits
    jf = JFloat(130.0)
    assert jf.byteValue() == -126
