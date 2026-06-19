from javalang.jfloat import JFloat

def test_jfloat_isnan():
    jf_nan = JFloat(float('nan'))
    jf_normal = JFloat(5.0)
    assert jf_nan.isNaN() == True
    assert jf_normal.isNaN() == False

def test_jfloat_isinfinite():
    jf_pos_inf = JFloat(float('inf'))
    jf_neg_inf = JFloat(float('-inf'))
    jf_normal = JFloat(10.5)
    assert jf_pos_inf.isInfinite() == True
    assert jf_neg_inf.isInfinite() == True
    assert jf_normal.isInfinite() == False

def test_jfloat_isfinite():
    assert JFloat.isFinite(10.5) == True
    assert JFloat.isFinite(float('inf')) == False
    assert JFloat.isFinite(float('nan')) == False
