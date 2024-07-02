import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check_mature():
    ret = -1
    for i in range(m):
        for j in range(n):
            if not graph[i][j]:
                return -1
            else:
                ret = max(ret, graph[i][j])
    return ret - 1

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(m)]
q = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(check_mature())