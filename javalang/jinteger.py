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