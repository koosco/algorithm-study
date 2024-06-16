import sys
from collections import deque
read = sys.stdin.readline

def find_connection(start_v: int):
    q = deque([start_v])
    visited.add(start_v)
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                q.append(w)

n, m = map(int, read().split())
graph = {i: [] for i in range(1, n + 1)}
visited = set()
res = 0

for _ in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

for v in range(1, n + 1):
    if v not in visited:
        find_connection(v)
        res += 1
print(res)