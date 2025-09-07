import algorithms.src.graphs as g


def test_bfs_basic():
    adj = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    order = g.bfs(adj, "A")
    assert order == ["A", "B", "C", "D", "E", "F"]
    assert len(order) == len(adj)


def test_bfs_disconnected():
    adj = {1: [2], 2: [1], 3: [4], 4: [3]}
    order = g.bfs(adj, 1)
    assert order == [1, 2]
