import algorithms.src.search as s


def test_binary_search_found():
    arr = [1, 2, 3, 4, 5, 8, 10]
    assert s.binary_search(arr, 4) == 3
    assert s.binary_search(arr, 1) == 0
    assert s.binary_search(arr, 10) == 6


def test_binary_search_not_found():
    arr = [1, 2, 3, 4, 5, 8, 10]
    assert s.binary_search(arr, 0) == -1
    assert s.binary_search(arr, 6) == -1
    assert s.binary_search(arr, 11) == -1


def test_binary_search_empty():
    assert s.binary_search([], 5) == -1
