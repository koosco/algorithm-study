import sys

MAX_SIZE = sys.maxsize

n = int(input())
dp = [MAX_SIZE] * 5001
dp[3] = 1; dp[5] = 1

for i in range(6, n+1):
    if dp[i-3] != MAX_SIZE:
        dp[i] = dp[i-3] + 1
    if dp[i-5] != -1:
        dp[i] = min(dp[i], dp[i-5] + 1)
print(dp[n] if dp[n] != MAX_SIZE else -1)