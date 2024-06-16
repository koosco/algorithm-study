import sys
from typing import List
from collections import deque

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def dfs(start_v: int, res: List[int]):
    res.append(start_v)
    dfs_visited.add(start_v)
    for v in graph[start_v]:
        if v not in dfs_visited:
            dfs(v, res)


def bfs(start_v: int, res: List[int]):
    q = deque()
    q.append(start_v)
    bfs_visited.add(start_v)
    while q:
        v = q.popleft()
        res.append(v)
        for w in graph[v]:
            if w not in bfs_visited:
                q.append(w)
                bfs_visited.add(w)


n, m, v = map(int, read().split())
graph = {i: [] for i in range(1, n + 1)}
dfs_visited, bfs_visited = set(), set()
dfs_res, bfs_res = [], []

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

for val in graph.values():
    val.sort()

dfs(v, dfs_res)
bfs(v, bfs_res)
print(*dfs_res); print(*bfs_res)