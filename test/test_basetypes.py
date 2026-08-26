

from intropy import add, Truc, Truc2, Step, Todo, InProgress, Done

import pytest

def test_add_ints():
    assert add(1,2) == 3

def test_add_strings():
    assert add("hello", "world") == "helloworld"

def test_add_lists():
    assert add([1,2,3,4], [5]) == [1,2,3,4,5]

def test_add_truc():
    assert Truc(1,2) + Truc(3,4) == Truc(4,6)

def test_add_truc2():
    assert Truc2(1,2) + Truc2(3,4) == Truc2(4,6)

def test_step():
    s = Step.new("Faire l'épicerie")

    s.start()
    s.stop()
    s.start()