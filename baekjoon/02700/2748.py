dp = [0, 1, 1] + [0] * 88

for i in range(3, 91):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[int(input())])