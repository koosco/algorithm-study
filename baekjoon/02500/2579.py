import sys
read = sys.stdin.readline

dp = [0] * 301
stairs = [0] * 301

n = int(read())
for i in range(1, n+1):
    stairs[i] = int(input())

dp[1] = stairs[1]; dp[2] = stairs[1] + stairs[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-2], stairs[i-1] + dp[i-3]) + stairs[i]
print(dp[n])