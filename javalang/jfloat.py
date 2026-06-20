from typing import Union

class JFloat:
    MAX_VALUE = 3.4028235e38
    MIN_VALUE = 1.4e-45
    MIN_NORMAL = 1.17549435e-38
    POSITIVE_INFINITY = float("inf")
    NEGATIVE_INFINITY = float("-inf")
    NaN = float("nan")
    SIZE = 32
    BYTES = 4

    def __init__(self, value: Union[float, int, str]):
        if isinstance(value, (float, int)):
            self.value = float(value)
        elif isinstance(value, str):
            try:
                self.value = float(value)
            except ValueError:
                raise ValueError(f"For input string: '{value}'")
        else:
            raise TypeError("Value must be a float, int or a numeric string")

    @staticmethod
    def parseFloat(s: str) -> float:
        """Equivalente ao Float.parseFloat(String s) do Java.
        Retorna um float primitivo do Python."""
        if not isinstance(s, str):
            raise TypeError("Argument must be a string")
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"For input string: '{s}'")

    @classmethod
    def valueOf(cls, value: Union[float, int, str]) -> "JFloat":
        """Equivalente ao Float.valueOf(float f) e Float.valueOf(String s) do Java.
        Retorna uma instância de JFloat."""
        if isinstance(value, (float, int)):
            return cls(value)
        elif isinstance(value, str):
            parsed_value = cls.parseFloat(value)
            return cls(parsed_value)
        else:
            raise TypeError("Value must be a float, int or a string")

    def intValue(self) -> int:
        """Equivalente ao Float.intValue() do Java.
        Retorna o valor interno convertido para int primitivo truncado."""
        return int(self.value)

    def longValue(self) -> int:
        """Equivalente ao Float.longValue() do Java."""
        return int(self.value)

    def byteValue(self) -> int:
        """Equivalente ao Float.byteValue() do Java, simulando overflow de byte."""
        return (int(self.value) + 128) % 256 - 128

    def floatValue(self) -> float:
        """Equivalente ao Float.floatValue() do Java."""
        return float(self.value)

    def doubleValue(self) -> float:
        """Equivalente ao Float.doubleValue() do Java.
        Em Python, retorna o mesmo tipo nativo float."""
        return float(self.value)

    def toString(self) -> str:
        """Equivalente ao Float.toString() do Java como método de instância."""
        return str(self.value)