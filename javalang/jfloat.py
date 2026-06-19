class JFloat:
    def __init__(self, value):
        self.value = float(value)

    def intValue(self):
        return int(self.value)

    def longValue(self):
        return int(self.value)

    def byteValue(self):
        # Simula o comportamento do byte em Java (limites de -128 a 127)
        return (int(self.value) + 128) % 256 - 128
