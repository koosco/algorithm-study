import sys
from typing import List

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def sol(i: int = 0, j: int = 0):
    if i == m - 1 and j == n - 1:
        return 1
    if dp[i][j] == -1:
        dp[i][j] = 0
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and graph[ni][nj] < graph[i][j]:
                dp[i][j] += sol(ni, nj)
    return dp[i][j]


m, n = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
print(sol())