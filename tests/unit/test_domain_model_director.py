import pytest

from domainmodel.director import Director

def test_init():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None

def test_eq_same():
    director1 = Director("Taika Waititi")
    director2 = Director("Taika Waititi")
    assert director1 == director2

def test_eq_not_same():
    director1 = Director("Taika Waititi")
    director2 = Director("Taika")
    assert director1 != director2

def test_lt_true():
    director1 = Director("aaa")
    director2 = Director("bbb")
    assert director1 < director2

def test_lt_same():
    director1 = Director("aaa")
    director2 = Director("aaa")
    assert (director1 < director2) == False

def test_hash_same():
    director1 = Director("aaa")
    director2 = Director("aaa")
    assert hash(director1) == hash(director2)

def test_hash_not_same():
    director1 = Director("aaa")
    director2 = Director("bbb")
    assert (hash(director1) == hash(director2)) == False