import math

class JFloat:
    def __init__(self, value):
        self.value = float(value)

    def isNaN(self):
        return math.isnan(self.value)

    def isInfinite(self):
        return math.isinf(self.value)

    @staticmethod
    def isFinite(f):
        return math.isfinite(float(f))
