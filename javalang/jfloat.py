def floatValue(self) -> float:
        """Equivalente ao Float.floatValue() do Java."""
        return float(self.value)

    def doubleValue(self) -> float:
        """Equivalente ao Float.doubleValue() do Java.
        No Python, retorna o mesmo tipo nativo 'float'."""
        return float(self.value)

    def toString(self) -> str:
        """Equivalente ao Float.toString() do Java (método de instância)."""
        return str(self.value)