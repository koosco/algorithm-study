import sys
from heapq import *
from typing import List, Tuple

read: callable = sys.stdin.readline

v, e = map(int, read().split())
visited = [False] * (v + 1)
res = 0
q = []
graph: List[List[Tuple[int, int]]] = [[] for _ in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
heappush(q, (0, 1))

while q:
    dist, now = heappop(q)
    if not visited[now]:
        visited[now] = True
        res += dist
        for node, cost in graph[now]:
            if not visited[node]:
                heappush(q, (cost, node))
print(res)

"""
6 10
1 2 2
1 3 3
2 3 4
2 4 1
2 5 7
3 5 1
3 4 3
4 5 2
4 6 5
5 6 4
"""