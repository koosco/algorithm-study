import sys
from collections import deque
read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def sol(i: int, j: int, ret: int):
    q = deque()
    q.append((i, j))
    visited.add((i, j))
    ret += 1
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and \
                (nx, ny) not in visited and not graph[nx][ny]:
                visited.add((nx, ny))
                q.append((nx, ny))
                ret += 1
    return ret

n, k = map(int, read().split())
graph = [list(map(int, read().split()))
            for _ in range(n)]
start_points = [tuple(map(lambda x: x-1, map(int, read().split())))
                for _ in range(k)]
visited = set()
res = 0

for point in start_points:
    if point not in visited:
        i, j = point
        res = sol(i, j, res)
print(res)