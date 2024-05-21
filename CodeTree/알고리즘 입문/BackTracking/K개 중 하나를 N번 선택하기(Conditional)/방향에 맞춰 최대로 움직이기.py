'''
3
7 1 4
2 6 3
9 8 5
5 3 1
6 3 7
2 4 8
3 3
'''

import sys
read = sys.stdin.readline

def sol(i: int, j: int, cnt: int):
    global res
    res = max(res, cnt)
    dx, dy = dir_map[directions[i][j]]
    for k in range(1, n):
        nx, ny = i + dx * k, j + dy * k
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[i][j]:
            sol(nx, ny, cnt + 1)

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
directions = [list(map(int, read().split())) for _ in range(n)]
r, c = map(lambda x:x-1, map(int, read().split()))
res = 0
dir_map = {
    1: (-1, 0),
    2: (-1, 1),
    3: (0, 1),
    4: (1, 1),
    5: (1, 0),
    6: (1, -1),
    7: (0, -1),
    8: (-1, -1)
}
sol(r, c, 0)
print(res)