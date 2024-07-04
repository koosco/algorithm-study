import sys

read = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def sol(i, j, depth=0, apple=0):
    graph[i][j] = -1
    if apple == 2:
        global res
        res += 1
        return
    if depth == 3:
        return

    for d in directions:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < 5 and 0 <= nj < 5:
            if graph[ni][nj] == 1:
                sol(ni, nj, depth + 1, apple+1)
                graph[ni][nj] = 1
            elif not graph[ni][nj]:
                sol(ni, nj, depth + 1, apple)
                graph[ni][nj] = 0


graph = [list(map(int, read().split())) for _ in range(5)]
r, c = map(int, read().split())
res = 0
sol(r, c)
print(1 if res else 0)
