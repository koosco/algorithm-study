import sys
from collections import deque
from typing import Tuple

read = sys.stdin.readline


def burning(start_f: Tuple[int, int]):
    q = deque([(i, j)])
    fires[i][j] = 1
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < r and 0 <= ny < c and not fires[nx][ny]:
                fires[nx][ny] = fires[x][y] + 1
                q.append((nx, ny))


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

r, c = map(int, read().split())
graph = [list(list(read().rstrip())) for _ in range(r)]
s, f = None, None
visited = set()
fires = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            s = (i, j)
        elif graph[i][j] == 'F':
            f = (i, j)

burning(f)
for row in fires:
    print(*row)