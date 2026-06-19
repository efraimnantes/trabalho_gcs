class JInteger:
    def __init__(self, value: int):
        self.value = value
    def doubleValue(self):
        return float(self.value)

    def byteValue(self):
        val = self.value & 0xFF
        return val if val < 128 else val - 256

    def shortValue(self):
        val = self.value & 0xFFFF
        return val if val < 32768 else val - 65536