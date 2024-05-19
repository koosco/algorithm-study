import sys
read = sys.stdin.readline

def find_top(col: int):
    for i in range(n):
        if graph[i][col] != 0:
            return i
    return -1

def bomb(x: int, y: int, mag: int):
    for i in range(-mag, mag+1):
        if 0 <= x + i < n:
            graph[x+i][y] = 0
        if 0 <= y + i < n:
            graph[x][y+i] = 0
    fall()

def fall():
    for j in range(n):
        tmp = []
        for i in range(n):
            if graph[i][j] != 0:
                tmp.append(graph[i][j])
        tmp = [0] * (n - len(tmp)) + tmp
        for i in range(n):
            graph[i][j] = tmp[i]

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
columns = [int(read()) for _ in range(m)]

for col in columns:
    row = find_top(col-1)
    if row != -1:
        bomb(row, col-1, graph[row][col-1]-1)

for row in graph:
    print(*row)