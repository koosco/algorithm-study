import sys
from typing import List
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_max_h():
    res = 0
    for row in graph:
        res = max(res, max(row))
    return res

def bfs(i: int, j: int, h: int):
    q = deque([(i, j)])
    visited.add((i, j))
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and \
                    graph[nx][ny] > h:
                visited.add((nx, ny))
                q.append((nx, ny))


n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
res = 1
for h in range(1, find_max_h()):
    semi_res = 0
    visited = set()
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited and graph[i][j] > h:
                bfs(i, j, h)
                semi_res += 1
    res = max(res, semi_res)
print(res)
