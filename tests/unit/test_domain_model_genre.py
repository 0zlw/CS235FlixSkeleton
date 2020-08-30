import pytest

from domainmodel.genre import Genre

def test_init():
    genre1 = Genre("Horror")
    assert repr(genre1) == "<Genre Horror>"
    genre2 = Genre("")
    assert genre2.genre_name is None
    genre3 = Genre(42)
    assert genre3.genre_name is None

def test_eq_same():
    genre1 = Genre("Comedy")
    genre2 = Genre("Comedy")
    assert genre1 == genre2

def test_eq_not_same():
    genre1 = Genre("Comedy")
    genre2 = Genre("Horror")
    assert genre1 != genre2

def test_lt_true():
    genre1 = Genre("Comedy")
    genre2 = Genre("Horror")
    assert genre1 < genre2

def test_lt_same():
    genre1 = Genre("Comedy")
    genre2 = Genre("Comedy")
    assert (genre1 < genre2) == False

def test_hash_same():
    genre1 = Genre("Comedy")
    genre2 = Genre("Comedy")
    assert hash(genre1) == hash(genre2)

def test_hash_not_same():
    genre1 = Genre("Comedy")
    genre2 = Genre("Horror")
    assert (hash(genre1) == hash(genre2)) == False