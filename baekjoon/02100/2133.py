n = int(input())
dp = [0] * 31

if n % 2:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = dp[i-2] * 3 + 2 + sum(dp[:i-3]) * 2
    print(dp[n])