def bubble_sort(arr):
    """Сортировка пузырьком. Возвращает новый отсортированный список."""
    result = list(arr)  # копия, чтобы не портить исходный список
    n = len(result)
    for i in range(n - 1):
        swapped = False  # меняли ли что-то за этот проход
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break  # обмена не было, значит уже всё отсортировано
    return result