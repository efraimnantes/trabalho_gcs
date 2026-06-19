# --- Novos testes para Formatação em Bases (Binary, Octal, Hex) ---

def test_to_binary_string():
    assert JInteger.toBinaryString(5) == "101"
    assert JInteger.toBinaryString(0) == "0"
    # Testa o comportamento do complemento de dois (32-bit) para negativos
    assert JInteger.toBinaryString(-1) == "11111111111111111111111111111111"

def test_to_octal_string():
    assert JInteger.toOctalString(8) == "10"
    assert JInteger.toOctalString(0) == "0"
    assert JInteger.toOctalString(-1) == "37777777777"

def test_to_hex_string():
    assert JInteger.toHexString(255) == "ff"
    assert JInteger.toHexString(0) == "0"
    assert JInteger.toHexString(-1) == "ffffffff"