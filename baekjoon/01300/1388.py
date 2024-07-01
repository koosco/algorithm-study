import sys
from collections import deque

read = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def sol(i, j):
    q = deque([(i, j)])
    visited.add((i, j))
    v = graph[i][j]
    while q:
        x, y = q.popleft()
        if v:
            nx, ny = x + 1, y
        else:
            nx, ny = x, y + 1
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and \
                graph[nx][ny] == v:
            visited.add((nx, ny))
            q.append((nx, ny))


n, m = map(int, read().split())
graph = [list(map(lambda x: {'-': 0, '|': 1}[x], list(read().rstrip()))) for _ in range(n)]
visited = set()
res = 0

for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            sol(i, j)
            res += 1
print(res)