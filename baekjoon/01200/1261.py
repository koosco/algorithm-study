import sys
from typing import List
from collections import deque

read = sys.stdin.readline
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

m, n = map(int, read().split())
graph: List[List[int]] = [list(map(int, list(read().rstrip()))) for _ in range(n)]
visited: List[List[int]] = [[0] * m for _ in range(n)]
visited[0][0] = 1
q = deque()
q.append((0, 0))

while q:
    y, x = q.popleft()
    for d in directions:
        ny, nx = y + d[0], x + d[1]
        if 0 <= ny < n and 0 <= nx < m and \
                not visited[ny][nx]:
            if graph[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
            else:
                q.appendleft((ny, nx))
                visited[ny][nx] = visited[y][x]

print(visited[-1][-1] - 1)
