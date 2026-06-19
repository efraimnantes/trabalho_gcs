class JInteger:
    def __init__(self, value: int):
        self.value = value
    def toString(self) -> str:
        return str(self.value)

    def equals(self, other) -> bool:
        if isinstance(other, JInteger):
            return self.value == other.value
        return False

    def compareTo(self, other) -> int:
        if not isinstance(other, JInteger):
            raise TypeError("Value must be a JInteger")

        if self.value < other.value:
            return -1
        if self.value > other.value:
            return 1
        return 0