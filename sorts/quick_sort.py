def quick_sort(arr):
    """Быстрая сортировка. Возвращает новый отсортированный список."""
    if len(arr) <= 1:
        return list(arr)  # нечего сортировать

    pivot = arr[len(arr) // 2]  # опорный элемент: берём из середины
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)