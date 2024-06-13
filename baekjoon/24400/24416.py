dp = [0, 1, 1] + [0] * 38

for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())
print(dp[n], n-2)