from __future__ import annotations

from typing import TypeAliasType


def add[T](a: T, b: TypeAliasType) -> T:
    return a + b
