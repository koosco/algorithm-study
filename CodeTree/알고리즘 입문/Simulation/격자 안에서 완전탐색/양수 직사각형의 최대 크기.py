import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
res = -1

def check(i: int, j: int, x: int, y: int):
    ret = 0
    for a in range(x+1):
        for b in range(y+1):
            if graph[i+a][j+b] <= 0:
                return False, -1
            else:
                ret += 1
    return True, ret


for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            for x in range(n-i):
                for y in range(m-j):
                    flag, ret = check(i, j, x, y)
                    if flag:
                        res = max(res, ret)
print(res)