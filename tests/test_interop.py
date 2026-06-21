from javalang.jinteger import JInteger
from javalang.jfloat import JFloat
from javalang.jstring import JString

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

def test_jstring_from_jinteger_value():
    jint = JInteger(42)
    # Testando criação a partir de valor textual
    jstr = JString(str(jint.value))
    assert jstr.value == "42"

def test_jstring_from_jfloat_value():
    jflt = JFloat(3.14)
    jstr = JString(str(jflt.value))
    assert jstr.value == "3.14"

def test_jstring_value_of_jinteger():
    jint = JInteger(100)
    # Testando valueOf com objeto JInteger (usa o __str__ que criamos)
    jstr = JString.valueOf(jint)
    assert jstr.value == "100"

def test_jstring_value_of_jfloat():
    jflt = JFloat(10.5)
    jstr = JString.valueOf(jflt)
    assert jstr.value == "10.5"