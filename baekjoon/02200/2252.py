import sys
from typing import List
from collections import deque

read: callable = sys.stdin.readline

n, m = map(int, read().split())
res: List[int] = []
degree: List[int] = [0] * (n + 1)
graph: List[List[int]] = [[] for _ in range(n + 1)]
q: deque[int] = deque()

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if not degree[i]:
        q.append(i)

while q:
    x: int = q.popleft()
    res.append(x)
    for node in graph[x]:
        degree[node] -= 1
        if not degree[node]:
            q.append(node)

print(*res)