from collections import deque


def bfs(adj, s):
    seen = {s}
    q = deque([s])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for w in adj.get(v, []):
            if w not in seen:
                seen.add(w)
                q.append(w)
    return order


# TODO: dfs, mst_kruskal, dijkstra
