n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(k)]
for i in range(k):
    dp[i][0] = 1
for j in range(n + 1):
    dp[0][j] = 1

for i in range(1, k):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_000
print(dp[-1][-1])