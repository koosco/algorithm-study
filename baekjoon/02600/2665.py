import sys
from typing import List, Tuple
from collections import deque

read = sys.stdin.readline
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def sol():
    n = int(read())
    graph: List[List[int]] = [list(map(int, list(read().rstrip()))) for _ in range(n)]
    dist: List[List[int]] = [[0] * n for _ in range(n)]
    q = deque([(0, 0)])
    dist[0][0] = 1

    while q:
        y, x = q.popleft()
        for d in directions:
            ny, nx = y + d[0], x + d[1]
            if 0 <= ny < n and 0 <= nx < n and not dist[ny][nx]:
                if graph[ny][nx]:
                    dist[ny][nx] = dist[y][x]
                    q.appendleft((ny, nx))
                else:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
    print(dist[-1][-1] - 1)


sol()
