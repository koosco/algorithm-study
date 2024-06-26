import sys
read = sys.stdin.readline

n = int(read())
graph = []
dp = [[0] * 500 for _ in range(500)]
for _ in range(n):
    graph.append(list(map(int, read().split())))

dp[0][0] = graph[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + graph[i][j]
print(max(dp[n-1]))