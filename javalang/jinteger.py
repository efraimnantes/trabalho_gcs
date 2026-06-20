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
    def parseInt(s: str, radix: int = 10) -> int:
        """Equivalente ao Integer.parseInt(String s) e Integer.parseInt(String s, int radix)."""
        if not isinstance(s, str):
            raise TypeError("Argument must be a string")

        if radix < 2 or radix > 36:
            raise ValueError(
                f"radix {radix} less than Character.MIN_RADIX "
                "or greater than Character.MAX_RADIX"
            )

        try:
            return int(s, radix)
        except ValueError:
            raise ValueError(f"For input string: '{s}' under radix {radix}")

    @classmethod
    def valueOf(cls, value: Union[int, str], radix: int = 10) -> "JInteger":
        """Equivalente ao Integer.valueOf com ou sem radix."""
        if isinstance(value, int):
            return cls(value)

        if isinstance(value, str):
            parsed_value = cls.parseInt(value, radix)
            return cls(parsed_value)

        raise TypeError("Value must be an int or a string")

    @classmethod
    def decode(cls, nm: str) -> "JInteger":
        """Equivalente ao Integer.decode(String nm) do Java."""
        if not isinstance(nm, str) or not nm:
            raise ValueError("Zero length string")

        sign = ""
        if nm[0] in ("-", "+"):
            sign = nm[0]
            nm = nm[1:]

        if not nm:
            raise ValueError("Zero length string")

        radix = 10
        if nm.startswith("0x") or nm.startswith("0X"):
            radix = 16
            nm = nm[2:]
        elif nm.startswith("#"):
            radix = 16
            nm = nm[1:]
        elif nm.startswith("0") and len(nm) > 1:
            radix = 8
            nm = nm[1:]

        try:
            parsed = int(nm, radix)
            if sign == "-":
                parsed = -parsed
            return cls(parsed)
        except ValueError:
            raise ValueError(f"For input string: '{sign}{nm}'")