import sys
from collections import deque

read = sys.stdin.readline


def bfs(i: int, j: int):
    q = deque([(i, j)])
    visited.add((i, j))
    while q:
        x, y = q.popleft()
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == 0 and c == 0:
                    continue
                nx, ny = x + r, y + c
                if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited and \
                        graph[nx][ny]:
                    visited.add((nx, ny))
                    q.append((nx, ny))


res = []
while True:
    w, h = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(h)]
    visited = set()
    semi_res = 0
    if w == 0 and h == 0:
        break
    for i in range(h):
        for j in range(w):
            if (i, j) not in visited and graph[i][j]:
                bfs(i, j)
                semi_res += 1
    res.append(str(semi_res))
print('\n'.join(res))