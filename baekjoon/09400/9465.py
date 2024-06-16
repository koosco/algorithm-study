import sys

read = sys.stdin.readline

res = []

for _ in range(int(read())):
    n = int(read())
    graph = [list(map(int, read().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]
    if n <= 1:
        res.append(str(max(dp[0][0], dp[1][0])))
        continue
    dp[0][1] = graph[1][0] + graph[0][1]
    dp[1][1] = graph[0][0] + graph[1][1]

    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + graph[0][j]
            if i == 1:
                dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + graph[1][j]

    res.append(str(max(dp[0][n - 1], dp[1][n - 1])))

print('\n'.join(res))
