from javalang.jfloat import JFloat


def test_jfloat_creation():
    value = JFloat(10.5)

    assert value.value == 10.5