import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def check(i, j, l):
    target = graph[i][j]
    for x in range(l):
        for y in range(l):
            if graph[i + x][j + y] != target:
                return False
    return str(target)


def sol(i, j, l):
    c = check(i, j, l)
    if c:
        return c
    ret = '('
    nl = l // 2
    ret += sol(i, j, nl)
    ret += sol(i, j + nl, nl)
    ret += sol(i + nl, j, nl)
    ret += sol(i + nl, j + nl, nl)
    return ret + ')'


n = int(read())
graph = [list(map(int, list(read().rstrip()))) for _ in range(n)]
print(sol(0, 0, n))
