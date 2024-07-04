import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
s, e = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
q = deque([s])
visited[s] = 1

for _ in range(int(read())):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)

while q:
    v = q.popleft()
    for w in graph[v]:
        if not visited[w]:
            visited[w] = visited[v] + 1
            q.append(w)
print(-1 if not visited[e] else visited[e] - 1)