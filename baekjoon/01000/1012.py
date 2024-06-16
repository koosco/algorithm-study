import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(i: int, j: int):
    q = deque([(i, j)])
    while q:
        r, c = q.popleft()
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc]:
                q.append((nr, nc))
                graph[nr][nc] = False

res = []
for T in range(int(read())):
    n, m, k = map(int, read().split())
    graph = [[False] * m for _ in range(n)]
    semi_res = 0
    for _ in range(k):
        x, y = map(int, read().split())
        graph[x][y] = True
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                bfs(i, j)
                semi_res += 1
    res.append(str(semi_res))
print('\n'.join(res))


