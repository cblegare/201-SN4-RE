from __future__ import annotations

def add(a, b):
    return a + b


class Truc:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __add__(self, other: Truc) -> Truc:
        return Truc(self.a + other.a, self.b + other.b)

    def __eq__(self, other: Truc) -> bool:
        return self.a == other.a and self.b == other.b


from typing import NamedTuple


class Truc2(NamedTuple):
    a: int
    b: int

    def __add__(self, other: Truc) -> Truc:
        return Truc(self.a + other.a, self.b + other.b)
