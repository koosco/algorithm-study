import sys

read = sys.stdin.readline


def sol(i: int, j: int, size: int):
    if graph[i][j] == graph[i + size][j] and graph[i][j] == graph[i][j + size] and \
            graph[i][j] == graph[i + size][j + size]:
        return (size + 1) ** 2
    return 0


n, m = map(int, read().split())
graph = [list(map(int, list(read().rstrip()))) for _ in range(n)]
max_size = min(n, m) - 1
res = 0
for size in range(max_size, -1, -1):
    for x in range(n):
        for y in range(m):
            if x + size < n and y + size < m:
                res = max(res, sol(x, y, size))
print(res)
