from typing import Union

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

    def contains(self, s) -> bool:
        if isinstance(s, JString):
            return s.value in self._value

        return str(s) in self._value

    def startsWith(self, prefix) -> bool:
        if isinstance(prefix, JString):
            return self._value.startswith(prefix.value)

        return self._value.startswith(str(prefix))

    def endsWith(self, suffix) -> bool:
        if isinstance(suffix, JString):
            return self._value.endswith(suffix.value)

        return self._value.endswith(str(suffix))
def indexOf(self, target: Union[str, int], fromIndex: int = 0) -> int:
        if isinstance(target, int):
            target_str = chr(target)
        elif isinstance(target, str):
            target_str = target
        else:
            raise TypeError("Target must be a string or an integer (Unicode code point)")
        
        return self.value.find(target_str, fromIndex)

def indexOf(self, target: Union[str, int], fromIndex: int = 0) -> int:
        if isinstance(target, int):
            target_str = chr(target)
        elif isinstance(target, str):
            target_str = target
        else:
            raise TypeError("Target must be a string or an integer (Unicode code point)")
        
        return self.value.find(target_str, fromIndex)

def lastIndexOf(self, target: Union[str, int], fromIndex: int = None) -> int:
    """
    Equivalente aos métodos do Java:
    - lastIndexOf(String str)
    - lastIndexOf(String str, int fromIndex)
    - lastIndexOf(int ch)
    - lastIndexOf(int ch, int fromIndex)
    """
    if isinstance(target, int):
        target_str = chr(target)
    elif isinstance(target, str):
        target_str = target
    else:
        raise TypeError("Target must be a string or an integer (Unicode code point)")
        
    if fromIndex is None:
        return self.value.rfind(target_str)
    else:
        limit = fromIndex + len(target_str)
        return self.value.rfind(target_str, 0, limit)