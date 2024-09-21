import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def check(i, j, l):
    target = graph[i][j]
    for x in range(l):
        for y in range(l):
            if graph[i + x][j + y] != target:
                return False
    res[target] += 1
    return True


def sol(i, j, l):
    if check(i, j, l):
        return
    nl = l // 3
    for x in range(3):
        for y in range(3):
            sol(i + nl * x, j + nl * y, nl)


n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
res = [0] * 3
sol(0, 0, n)
print(res[-1], res[0], res[1], sep='\n')