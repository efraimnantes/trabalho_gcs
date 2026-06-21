class JString:
    """Adaptação inicial da classe java.lang.String para Python."""

    _slots_ = ("_value",)

    def _init_(self, value="") -> None:
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

    def length(self) -> int:
        return len(self._value)

    def isEmpty(self) -> bool:
        return self.length() == 0

    def charAt(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("String index out of range")

        return self._value[index]

    def toLowerCase(self):
        return JString(self._value.lower())

    def toUpperCase(self):
        return JString(self._value.upper())

    def trim(self):
        return JString(self._value.strip())