from typing import Union

class JInteger:
    # Constantes da especificação Java SE 8 (32-bit signed integer)
    MAX_VALUE: int = 2147483647
    MIN_VALUE: int = -2147483648
    SIZE: int = 32
    BYTES: int = 4
    TYPE = int  # Adaptação: mapeia para o tipo primitivo int do Python

    def __init__(self, value: Union[int, str]):
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
    def parseInt(s: str) -> int:
        """Equivalente ao Integer.parseInt(String s) do Java.
        Retorna um int primitivo do Python."""
        if not isinstance(s, str):
            raise TypeError("Argument must be a string")
        try:
            return int(s)
        except ValueError:
            raise ValueError(f"For input string: '{s}'")

    @classmethod
    def valueOf(cls, value: Union[int, str]) -> 'JInteger':
        """Equivalente ao Integer.valueOf(int i) e Integer.valueOf(String s) do Java.
        Retorna uma instância de JInteger."""
        if isinstance(value, int):
            return cls(value)
        elif isinstance(value, str):
            # O Java internamente chama o parseInt e encapsula no objeto
            parsed_value = cls.parseInt(value)
            return cls(parsed_value)
        else:
            raise TypeError("Value must be an int or a string")