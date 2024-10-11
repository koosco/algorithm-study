import sys
from heapq import *
from typing import List

read: callable = sys.stdin.readline

n, m = map(int, read().split())
graph: List[List[int]] = [[] for _ in range(n + 1)]
degree: List[int] = [0] * (n + 1)
q: List[int] = []
res: List[int] = []

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if not degree[i]:
        heappush(q, i)
while q:
    x: int = heappop(q)
    res.append(x)
    for node in graph[x]:
        degree[node] -= 1
        if not degree[node]:
            heappush(q, node)

print(*res)