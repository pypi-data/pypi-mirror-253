from sympy import Symbol


class QmodSizedProxy(Symbol):
    def __new__(cls, name, **assumptions):
        return super().__new__(cls, name, **assumptions)

    def __init__(self, name: str, size: int) -> None:
        self._size = size

    @property
    def size(self) -> int:
        return self.args[0]

    def __len__(self) -> int:
        return self._size
