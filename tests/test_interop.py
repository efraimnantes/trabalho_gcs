from javalang.jfloat import JFloat
from javalang.jinteger import JInteger
from javalang.jstring import JString


def test_classes_can_be_instantiated_together():
    integer_value = JInteger(10)
    string_value = JString("10")
    float_value = JFloat(10.0)

    assert integer_value.value == 10
    assert string_value.value == "10"
    assert float_value.value == 10.0