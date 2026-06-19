@staticmethod
def toBinaryString(i: int) -> str:
    """Equivalente ao Integer.toBinaryString(int i) do Java."""
    if not isinstance(i, int):
        raise TypeError("Argument must be an integer")
    # Usa máscara de 32-bit para simular o comportamento unsigned do Java com negativos
    return bin(i & 0xFFFFFFFF)[2:]

@staticmethod
def toOctalString(i: int) -> str:
    """Equivalente ao Integer.toOctalString(int i) do Java."""
    if not isinstance(i, int):
        raise TypeError("Argument must be an integer")
    return oct(i & 0xFFFFFFFF)[2:]

@staticmethod
def toHexString(i: int) -> str:
    """Equivalente ao Integer.toHexString(int i) do Java."""
    if not isinstance(i, int):
        raise TypeError("Argument must be an integer")
    return hex(i & 0xFFFFFFFF)[2:]