class JInteger:
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def sum(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def max(a: int, b: int) -> int:
        if a >= b:
            return a
        return b

    @staticmethod
    def min(a: int, b: int) -> int:
        if a <= b:
            return a
        return b