from typing import Union

class JString:
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        self.value = value

    def indexOf(self, target: Union[str, int], fromIndex: int = 0) -> int:
        """
        Equivalente aos métodos do Java:
        - indexOf(String str)
        - indexOf(String str, int fromIndex)
        - indexOf(int ch)
        - indexOf(int ch, int fromIndex)
        """
        if isinstance(target, int):
            # No Java, indexOf(int) procura pelo código Unicode do caractere
            target_str = chr(target)
        elif isinstance(target, str):
            target_str = target
        else:
            raise TypeError("Target must be a string or an integer (Unicode code point)")
        
        # O .find() do Python retorna o índice ou -1 se não encontrar (igual ao Java)
        return self.value.find(target_str, fromIndex)