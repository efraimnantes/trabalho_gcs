
class JInteger:
    MAX_VALUE: int = 2147483647
    MIN_VALUE: int = -2147483648
    SIZE: int = 32
    BYTES: int = 4
    TYPE = int

    def __init__(self, value: int | str):
        if isinstance(value, str):
            try:
                self.value = int(value)
            except ValueError:
                raise ValueError(f"For input string: '{value}'")
        elif isinstance(value, int):
            self.value = value
        else:
            raise TypeError("Value must be an int or a numeric string")

    @staticmethod
    def compare(x: int, y: int) -> int:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Arguments must be integers")

        if x < y:
            return -1
        if x > y:
            return 1
        return 0

    @staticmethod
    def compareUnsigned(x: int, y: int) -> int:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Arguments must be integers")

        ux = x & 0xFFFFFFFF
        uy = y & 0xFFFFFFFF

        if ux < uy:
            return -1
        if ux > uy:
            return 1
        return 0

    @staticmethod
    def toUnsignedString(i: int) -> str:
        if not isinstance(i, int):
            raise TypeError("Argument must be an integer")

        return str(i & 0xFFFFFFFF)
