from typing import Union

class JFloat:
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
    def valueOf(cls, value: Union[float, int, str]) -> 'JFloat':
        """Equivalente ao Float.valueOf(float f) e Float.valueOf(String s) do Java.
        Retorna uma instância de JFloat."""
        if isinstance(value, (float, int)):
            return cls(value)
        elif isinstance(value, str):
            parsed_value = cls.parseFloat(value)
            return cls(parsed_value)
        else:
            raise TypeError("Value must be a float, int or a string")