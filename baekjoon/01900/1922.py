import sys
from typing import Tuple, List
from heapq import *

read: callable = sys.stdin.readline

n, m = int(read()), int(read())
res: int = 0
visited: List[bool] = [False] * (n + 1)
graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q: List[Tuple[int, int]] = [(0, 1)]
while q:
    dist, now = heappop(q)
    if not visited[now]:
        visited[now] = True
        res += dist
        for node, cost in graph[now]:
            if not visited[node]:
                heappush(q, (cost, node))
print(res)
