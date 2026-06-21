class JString:
    """Adaptação inicial da classe java.lang.String para Python."""

    __slots__ = ("_value",)

    def __init__(self, value="") -> None:
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

    def equals(self, anObject: object) -> bool:
        if isinstance(anObject, JString):
            return self._value == anObject._value
        if isinstance(anObject, str):
            return self._value == anObject
        return False

    def equalsIgnoreCase(self, anotherString: "JString | str") -> bool:
        if isinstance(anotherString, JString):
            return self._value.lower() == anotherString._value.lower()
        if isinstance(anotherString, str):
            return self._value.lower() == anotherString.lower()
        return False

    def __hash__(self) -> int:
        # No Python, para adaptar o hashCode() do Java de forma nativa,
        # implementamos o método especial __hash__
        return hash(self._value)

    def contains(self, s):
        if isinstance(s, JString):
            return s._value in self._value
        return str(s) in self._value

    def startsWith(self, prefix):
        if isinstance(prefix, JString):
            return self._value.startswith(prefix._value)
        return self._value.startswith(str(prefix))

    def endsWith(self, suffix):
        if isinstance(suffix, JString):
            return self._value.endswith(suffix._value)
        return self._value.endswith(str(suffix))
