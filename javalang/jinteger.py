@staticmethod
def compare(x: int, y: int) -> int:
    """Equivalente ao Integer.compare(int x, int y) do Java."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Arguments must be integers")
    if x < y:
        return -1
    elif x > y:
        return 1
    return 0

@staticmethod
def compareUnsigned(x: int, y: int) -> int:
    """Equivalente ao Integer.compareUnsigned(int x, int y) do Java."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Arguments must be integers")
    # Aplica máscara de 32-bit para simular o comportamento unsigned do Java
    ux = x & 0xFFFFFFFF
    uy = y & 0xFFFFFFFF
    if ux < uy:
        return -1
    elif ux > uy:
        return 1
    return 0

@staticmethod
def toUnsignedString(i: int) -> str:
    """Equivalente ao Integer.toUnsignedString(int i) do Java."""
    if not isinstance(i, int):
        raise TypeError("Argument must be an integer")
    return str(i & 0xFFFFFFFF)