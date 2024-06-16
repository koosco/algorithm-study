import sys

read = sys.stdin.readline

n = int(read())
pays = [0] + list(tuple(map(int, read().split())) for _ in range(n))
dp = [0] * 16

for i, pay in enumerate(pays[1:]):
    t, p = pay
    dp[i] = max(dp[i], dp[i - 1])
    if i + t < n + 1:
        dp[i + t] = max(dp[i + t], dp[i] + p)
print(max(dp))
