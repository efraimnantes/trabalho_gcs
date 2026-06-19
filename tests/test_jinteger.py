# --- Novos testes para Parsing com Radix e Decode ---

def test_parse_int_with_radix():
    # Base 2 (Binário)
    assert JInteger.parseInt("1010", 2) == 10
    # Base 8 (Octal)
    assert JInteger.parseInt("12", 8) == 10
    # Base 10 (Decimal)
    assert JInteger.parseInt("10", 10) == 10
    # Base 16 (Hexadecimal)
    assert JInteger.parseInt("A", 16) == 10
    assert JInteger.parseInt("-FF", 16) == -255

def test_parse_int_invalid_radix():
    with pytest.raises(ValueError):
        JInteger.parseInt("10", 1)  # Menor que MIN_RADIX (2)
    with pytest.raises(ValueError):
        JInteger.parseInt("10", 37) # Maior que MAX_RADIX (36)

def test_value_of_with_radix():
    obj = JInteger.valueOf("1010", 2)
    assert isinstance(obj, JInteger)
    assert obj.value == 10

def test_decode_valid_prefixes():
    # Hexadecimal com 0x e 0X
    assert JInteger.decode("0x10").value == 16
    assert JInteger.decode("-0X10").value == -16
    # Hexadecimal com #
    assert JInteger.decode("#10").value == 16
    # Octal com 0
    assert JInteger.decode("010").value == 8
    assert JInteger.decode("-010").value == -8
    # Decimal
    assert JInteger.decode("10").value == 10
    assert JInteger.decode("+10").value == 10

def test_decode_invalid_strings():
    with pytest.raises(ValueError):
        JInteger.decode("") # Vazio
    with pytest.raises(ValueError):
        JInteger.decode("-") # Apenas sinal
    with pytest.raises(ValueError):
        JInteger.decode("0xG") # Hex inválido