import sys
read = sys.stdin.readline

n = int(read())
wines = [0] * 10_001
dp = [0] * 10_001

for i in range(1, n+1):
    wines[i] = int(read())

dp[1] = wines[1]; dp[2] = wines[1] + wines[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], wines[i] + dp[i-2], wines[i] + wines[i-1] + dp[i-3])
print(dp[n])