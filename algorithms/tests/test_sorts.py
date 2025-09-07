import random, algorithms.src.sorts as s


def test_quicksort_basic():
    arr = [5, 1, 4, 2, 3]
    assert s.quicksort(arr) == [1, 2, 3, 4, 5]


def test_stability_like():  # 고난도는 추후
    arr = [2, 2, 1, 1, 3]
    assert s.quicksort(arr) == sorted(arr)
