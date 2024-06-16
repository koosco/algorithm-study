import sys
from collections import deque

read = sys.stdin.readline


def check(idx1, idx2):
    if 0 <= idx1 < n and 0 <= idx2 < n:
        for i in range(m):
            if graph[idx1][i] == graph[idx2][i]:
                return True
    return False


def shift(idx, lr, ud):
    graph[idx].rotate(lr)
    if ud in (0, -1) and check(idx, idx - 1):
        shift(idx - 1, -lr, -1)
    if ud in (0, 1) and check(idx, idx + 1):
        shift(idx + 1, -lr, 1)


n, m, q = map(int, read().split())
graph = [deque(map(int, read().split())) for _ in range(n)]
queries = list(map(lambda query: [int(query[0]) - 1, {'L': 1, 'R': -1}[query[1]]],
                   [read().split() for _ in range(q)]))
for query in queries:
    shift(query[0], query[1], 0)
for row in graph:
    print(*row)
