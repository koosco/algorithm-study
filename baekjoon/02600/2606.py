import sys
from collections import deque
from typing import List

read = sys.stdin.readline


def bfs(res: List[int], start_v: int = 1):
    q = deque([start_v])
    visited.add(start_v)
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                q.append(w)
                res.append(w)


n, m = int(read()), int(read())
graph = {i: [] for i in range(1, n + 1)}
visited = set()
res = []
for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)
bfs(res)
print(len(res))
