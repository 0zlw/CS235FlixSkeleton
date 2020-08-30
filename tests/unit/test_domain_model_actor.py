import pytest

from domainmodel.actor import Actor

def test_init():
    actor1 = Actor("Brad Pitt")
    assert repr(actor1) == "<Actor Brad Pitt>"
    actor2 = Actor("")
    assert actor2.actor_full_name is None
    actor3 = Actor(42)
    assert actor3.actor_full_name is None

def test_eq_same():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Brad Pitt")
    assert actor1 == actor2

def test_eq_not_same():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Brad")
    assert actor1 != actor2

def test_lt_true():
    actor1 = Actor("aaa")
    actor2 = Actor("bbb")
    assert actor1 < actor2

def test_lt_same():
    actor1 = Actor("aaa")
    actor2 = Actor("aaa")
    assert (actor1 < actor2) == False

def test_hash_same():
    actor1 = Actor("aaa")
    actor2 = Actor("aaa")
    assert hash(actor1) == hash(actor2)

def test_hash_not_same():
    actor1 = Actor("aaa")
    actor2 = Actor("bbb")
    assert (hash(actor1) == hash(actor2)) == False

def test_add_actor_colleague():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    actor1.add_actor_colleague(actor2)
    actor2.add_actor_colleague(actor1)

def test_actor_has_colleague():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor2)

def test_actor_has_no_colleagues():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    assert actor1.check_if_this_actor_worked_with(actor2) == False

def test_actor_has_not_worked_with_colleague():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Angelina Jolie")
    actor3 = Actor("Tom Hanks")
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor3) == False