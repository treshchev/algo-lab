import pytest
from ds.array import Array


def test_append_and_get():
    a = Array()
    a.append(5)
    a.append(7)
    assert a.get(0) == 5
    assert a.get(1) == 7
    assert len(a) == 2


def test_insert():
    a = Array()
    a.append(5)
    a.append(7)
    a.insert(1, 6)
    assert a.data == [5, 6, 7]


def test_remove_at():
    a = Array()
    a.append(1)
    a.append(2)
    a.remove_at(0)
    assert a.data == [2]


def test_set():
    a = Array()
    a.append(1)
    a.set(0, 9)
    assert a.get(0) == 9


def test_find():
    a = Array()
    a.append(4)
    a.append(8)
    assert a.find(8) == 1
    assert a.find(100) == -1


def test_wrong_index():
    a = Array()
    with pytest.raises(IndexError):
        a.get(0)
    with pytest.raises(IndexError):
        a.remove_at(0)