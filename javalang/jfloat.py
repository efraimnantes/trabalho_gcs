class JFloat:
    MAX_VALUE = 3.4028235e38
    MIN_VALUE = 1.4e-45
    MIN_NORMAL = 1.17549435e-38
    POSITIVE_INFINITY = float('inf')
    NEGATIVE_INFINITY = float('-inf')
    NaN = float('nan')
    SIZE = 32
    BYTES = 4

    def __init__(self, value):
        self.value = float(value)
