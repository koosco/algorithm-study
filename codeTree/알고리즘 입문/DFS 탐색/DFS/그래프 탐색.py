import sys
from collections import deque
read = sys.stdin.readline

def sol(v: int=1):
    q = deque()
    res = 0
    q.append(v)
    visited.add(v)
    while q:
        x = q.popleft()
        for elem in graph[x]:
            if elem not in visited:
                q.append(elem)
                visited.add(elem)
                res += 1
    return res


n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = set()
for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

print(sol())