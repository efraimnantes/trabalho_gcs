class JInteger:
    def __init__(self, value: int):
        self.value = value
    def intValue(self):
        return self.value

    def longValue(self):
        return self.value

    def floatValue(self):
        return float(self.value)