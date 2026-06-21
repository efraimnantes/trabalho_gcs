from __future__ import annotations


class JString:
    """Adaptação inicial da classe java.lang.String para Python."""

    __slots__ = ("_value",)

    def __init__(self, value: str | JString | None = "") -> None:
        if value is None:
            self._value = ""
            return

        if isinstance(value, JString):
            self._value = value.value
            return

        if not isinstance(value, str):
            raise TypeError("JString value must be a string")

        self._value = value

    @property
    def value(self) -> str:
        return self._value