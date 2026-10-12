from ds.avl_tree import AVLTree


def test_insert_and_find():
    t = AVLTree()
    for x in [5, 3, 8, 1, 4]:
        t.insert(x)
    assert t.to_list() == [1, 3, 4, 5, 8]
    assert t.find(4) is True
    assert t.find(7) is False


def test_duplicates():
    t = AVLTree()
    t.insert(1)
    t.insert(1)
    assert t.to_list() == [1]


def test_balance_ascending():
    t = AVLTree()
    for x in range(1, 8):
        t.insert(x)
    assert t.to_list() == [1, 2, 3, 4, 5, 6, 7]
    assert t.height() == 3
    assert t.root.value == 4


def test_balance_descending():
    t = AVLTree()
    for x in range(7, 0, -1):
        t.insert(x)
    assert t.height() == 3
    assert t.root.value == 4


def test_left_right_case():
    t = AVLTree()
    for x in [3, 1, 2]:
        t.insert(x)
    assert t.root.value == 2


def test_right_left_case():
    t = AVLTree()
    for x in [1, 3, 2]:
        t.insert(x)
    assert t.root.value == 2


def test_empty():
    t = AVLTree()
    assert t.to_list() == []
    assert t.height() == 0
    assert t.find(1) is False