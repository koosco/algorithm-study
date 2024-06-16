import sys
from collections import deque

read = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_apart(i: int, j: int):
    q = deque()
    q.append((i, j))
    visited.add((i, j))
    ret = 1
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and \
                    graph[nx][ny]:
                visited.add((nx, ny))
                q.append((nx, ny))
                ret += 1
    return ret


n = int(read())
graph = [list(map(int, list(read().rstrip()))) for _ in range(n)]
visited = set()
res = []

for i in range(n):
    for j in range(n):
        if (i, j) not in visited and graph[i][j]:
            res.append(find_apart(i, j))

print(len(res), '\n'.join(map(str, sorted(res))))
