import sys

read = sys.stdin.readline
INF = int(1e9)

n, k = map(int, read().split())
coins = sorted([int(read()) for _ in range(n)])
dp = [INF] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i-coin] + 1)
print(dp[-1] if dp[-1] != INF else -1)
