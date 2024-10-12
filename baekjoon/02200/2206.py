import sys
from collections import deque
from typing import List, Tuple

read = sys.stdin.readline
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(i: int = 0, j: int = 0):
    q: deque[Tuple[int, int, int]] = deque([(i, j, 0)])
    visited[i][j][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z]:
                if not graph[nx][ny] and not visited[nx][ny][z]:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                elif graph[nx][ny] and z == 0:
                    q.append((nx, ny, z + 1))
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
    return -1


n, m = map(int, read().split())
graph: List[List[int]] = [list(map(int, list(read().rstrip()))) for _ in range(n)]
visited: List[List[List[int]]] = [[[0, 0] for _ in range(m)] for _ in range(n)]
print(bfs())

