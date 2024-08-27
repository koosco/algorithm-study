import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def check(i, j, l):
    target = graph[i][j]
    for x in range(l):
        for y in range(l):
            if graph[i + x][j + y] != target:
                return False
    global b, w
    if target:
        b += 1
    else:
        w += 1
    return True


def sol(i: int, j: int, l: int):
    if check(i, j, l):
        return
    nl = l // 2
    sol(i, j, nl)
    sol(i, j + nl, nl)
    sol(i + nl, j, nl)
    sol(i + nl, j + nl, nl)


n = int(read())
graph = [list(map(lambda x: {'1': True, '0': False}[x], read().split())) for _ in range(n)]
b, w = 0, 0
sol(0, 0, n)
print(w, b, sep='\n')
