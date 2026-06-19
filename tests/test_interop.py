import pytest
from javalang.jinteger import JInteger
from javalang.jfloat import JFloat

def test_jinteger_to_float_compatible():
    jint = JInteger(123)
    # Testa a conversão explícita usando floatValue()
    assert jint.floatValue() == 123.0
    assert isinstance(jint.floatValue(), float)

def test_jfloat_from_integer_value():
    jint = JInteger(42)
    # Criando JFloat a partir do valor interno (int) de um JInteger
    jfloat = JFloat(jint.value)
    assert jfloat.value == 42.0

    # Criando JFloat diretamente de um int primitivo
    jfloat_primitive = JFloat(100)
    assert jfloat_primitive.value == 100.0

def test_simple_operations_between_wrappers():
    jint = JInteger(10)
    jfloat = JFloat(5.5)

    # Operações aritméticas simples simulando unboxing via .value
    soma = jint.value + jfloat.value
    subtracao = jfloat.value - jint.value
    multiplicacao = jint.value * jfloat.value

    assert soma == 15.5
    assert subtracao == -4.5
    assert multiplicacao == 55.0

def test_jfloat_to_integer_compatible():
    jfloat = JFloat(9.99)
    # Trunca o valor ao converter para int, igual ao comportamento Java
    assert jfloat.intValue() == 9
    assert isinstance(jfloat.intValue(), int)