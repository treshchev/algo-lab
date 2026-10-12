import pytest
from ds.deque import Deque


def test_push_and_pop():
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    d.push_front(0)
    assert d.to_list() == [0, 1, 2]
    assert d.pop_front() == 0
    assert d.pop_back() == 2
    assert d.to_list() == [1]


def test_peek():
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    assert d.peek_front() == 1
    assert d.peek_back() == 2
    assert len(d) == 2  # peek ничего не удаляет


def test_single_element():
    d = Deque()
    d.push_front(5)
    assert d.pop_back() == 5
    assert d.is_empty()
    d.push_back(6)  # дек должен работать и после опустошения
    assert d.to_list() == [6]


def test_empty_errors():
    d = Deque()
    with pytest.raises(IndexError):
        d.pop_front()
    with pytest.raises(IndexError):
        d.pop_back()
    with pytest.raises(IndexError):
        d.peek_front()
    with pytest.raises(IndexError):
        d.peek_back()