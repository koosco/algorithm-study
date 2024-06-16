import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[0] * (n + 1)] + [[0] + list(map(int, read().split())) for _ in range(n)]
queries = [list(map(int, read().split())) for _ in range(m)]
dp = [[0] * (n + 1) for _ in range(n + 1)]
res = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i][j]
for query in queries:
    x1, y1, x2, y2 = query
    res.append(str(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]))
print('\n'.join(res))