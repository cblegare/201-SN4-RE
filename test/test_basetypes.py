from __future__ import annotations

from intropy.basetypes import add


def test_add_ints():
    assert add(1, 2) == 3


def test_add_strings():
    assert add("hello", "world") == "helloworld"


def test_add_lists():
    assert add([1, 2, 3, 4], [5]) == [1, 2, 3, 4, 5]
