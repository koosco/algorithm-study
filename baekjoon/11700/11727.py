dp = [0, 1, 3] + [0] * 998

for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10_007

print(dp[int(input())])