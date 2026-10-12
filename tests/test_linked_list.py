from ds.linked_list import LinkedList


def test_add_first_and_last():
    l = LinkedList()
    l.add_last(1)
    l.add_last(2)
    l.add_first(0)
    assert l.to_list() == [0, 1, 2]
    assert len(l) == 3


def test_remove_middle():
    l = LinkedList()
    for x in [0, 1, 2]:
        l.add_last(x)
    assert l.remove(1) is True
    assert l.to_list() == [0, 2]


def test_remove_first():
    l = LinkedList()
    l.add_last(1)
    l.add_last(2)
    l.remove(1)
    assert l.to_list() == [2]


def test_remove_missing():
    l = LinkedList()
    l.add_last(1)
    assert l.remove(5) is False
    assert len(l) == 1


def test_find():
    l = LinkedList()
    l.add_last(3)
    assert l.find(3) is True
    assert l.find(4) is False


def test_empty():
    l = LinkedList()
    assert l.to_list() == []
    assert len(l) == 0