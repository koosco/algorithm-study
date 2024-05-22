import sys
from collections import deque
read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def get_max_k():
    ret = 0
    for i in range(n):
        for j in range(m):
            ret = max(ret, graph[i][j])
    return ret

def sol(i: int, j: int, k: int):
    q = deque()
    q.append((i, j))
    visited.add((i, j))
    ret = 0

    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and\
                (nx, ny) not in visited and graph[nx][ny] > k:
                q.append((nx, ny))
                visited.add((nx, ny))
                ret += 1
    return ret

n, m = map(int, read().split())
graph = [list(map(int, read().split()))
            for _ in range(n)]
max_k, max_safe_size = 1, 0
for k in range(1, get_max_k()):
    visited = set()
    safe_zone = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and graph[i][j] > k:
                sol(i, j, k)
                safe_zone += 1
    if safe_zone > max_safe_size:
        max_safe_size = safe_zone
        max_k = k
print(max_k, max_safe_size)