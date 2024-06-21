import sys

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[0] * (m+1)] + [[0] + list(map(int, read().split())) for _ in range(n)]
queries = [list(map(int, read().split())) for _ in range(int(read()))]
dp = [[0] * (m+1) for _ in range(n+1)]
res = []
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]
for x1, y1, x2, y2 in queries:
    res.append(str(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]))
print('\n'.join(res))