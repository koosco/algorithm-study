dp = [[0] * 10 for _ in range(101)]

dp[1] = [0] + [1] * 9
n = int(input())
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1_000_000_000)