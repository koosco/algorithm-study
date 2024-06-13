import sys
from collections import deque
read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def sol(i: int=0, j: int=0):
    q = deque()
    q.append((i, j))
    visited.add((i, j))

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return True
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and \
                (nx, ny) not in visited and graph[nx][ny]:
                visited.add((nx, ny))
                q.append((nx, ny))
    return False

n, m = map(int, read().split())
graph = [list(map(int, read().split()))
            for _ in range(n)]
visited = set()
print(1 if sol() else 0)