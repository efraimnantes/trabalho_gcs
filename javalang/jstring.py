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
            return self._value == anObject.value

        if isinstance(anObject, str):
            return self._value == anObject

        return False

    def equalsIgnoreCase(self, anotherString: "JString | str") -> bool:
        if isinstance(anotherString, JString):
            return self._value.lower() == anotherString.value.lower()

        if isinstance(anotherString, str):
            return self._value.lower() == anotherString.lower()

        return False

    def hashCode(self) -> int:
        return hash(self._value)

    def __hash__(self) -> int:
        return self.hashCode()

    def substring(self, beginIndex: int, endIndex=None):
        if beginIndex < 0 or beginIndex > len(self._value):
            raise IndexError("String index out of range")

        if endIndex is None:
            return JString(self._value[beginIndex:])

        if endIndex < beginIndex or endIndex > len(self._value):
            raise IndexError("String index out of range")

        return JString(self._value[beginIndex:endIndex])

    def subSequence(self, beginIndex: int, endIndex: int):
        return self.substring(beginIndex, endIndex)

    def concat(self, str_to_concat):
        if isinstance(str_to_concat, JString):
            return JString(self._value + str_to_concat.value)

        return JString(self._value + str(str_to_concat))

    def replace(self, target, replacement):
        return JString(self._value.replace(str(target), str(replacement)))
