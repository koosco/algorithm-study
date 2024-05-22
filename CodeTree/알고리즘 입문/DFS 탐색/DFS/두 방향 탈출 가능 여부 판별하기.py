import sys
read = sys.stdin.readline

directions = [(1, 0), (0, 1)]

def sol(i: int, j: int):
    global res
    if i == n - 1 and j == m - 1:
        res = 1
        return
    visited.add((i, j))
    for d in directions:
        nx, ny = i + d[0], j + d[1]
        if not res and 0 <= nx < n and 0 <= ny < m and\
            graph[nx][ny] and (nx, ny) not in visited:
                sol(nx, ny)
                

n, m = map(int, read().split())
graph = [list(map(int, read().split()))
            for _ in range(n)]
visited = set()
res = 0
sol(0, 0)
print(res)