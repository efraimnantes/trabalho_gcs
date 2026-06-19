# --- Novos testes para Conversões Simples ---

def test_float_value():
    obj = JFloat("3.14")
    assert obj.floatValue() == 3.14
    assert isinstance(obj.floatValue(), float)

def test_double_value():
    # Em Python, float engloba a precisão do double
    obj = JFloat(2.71828)
    assert obj.doubleValue() == 2.71828
    assert isinstance(obj.doubleValue(), float)

def test_to_string():
    obj = JFloat(10.5)
    assert obj.toString() == "10.5"
    assert isinstance(obj.toString(), str)
    
    obj_zero = JFloat(0.0)
    assert obj_zero.toString() == "0.0"