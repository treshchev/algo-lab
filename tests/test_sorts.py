import random
from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort


def check_sort(sort):
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert sort([1, 2, 3]) == [1, 2, 3]  # уже отсортирован
    assert sort([3, 2, 1]) == [1, 2, 3]  # в обратном порядке
    assert sort([2, 2, 2]) == [2, 2, 2]  # все одинаковые
    assert sort([-3, 0, 5, -1]) == [-3, -1, 0, 5]  # отрицательные


def test_bubble_sort():
    check_sort(bubble_sort)


def test_quick_sort():
    check_sort(quick_sort)


def test_original_not_changed():
    data = [3, 1, 2]
    bubble_sort(data)
    quick_sort(data)
    assert data == [3, 1, 2]


def test_random_compare_with_builtin():
    for _ in range(50):
        data = [random.randint(-100, 100) for _ in range(random.randint(0, 30))]
        assert bubble_sort(data) == sorted(data)
        assert quick_sort(data) == sorted(data)