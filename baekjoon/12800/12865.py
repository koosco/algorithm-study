import sys

read = sys.stdin.readline

n, k = map(int, read().split())
items = [list(map(int, read().split())) for _ in range(n)]
dp = [0] * (k + 1)
for w, v in items:
    for i in range(k, w-1, -1):
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])
