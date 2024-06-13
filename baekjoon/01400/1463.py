import sys
MAX_SIZE = sys.maxsize

dp = [0] * (int(1e6) + 1)
dp[2] = 1; dp[3] = 1

N = int(input())
for i in range(4, N+1):
    dp[i] = dp[i-1]
    if i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i])
    dp[i] += 1
print(dp[N])