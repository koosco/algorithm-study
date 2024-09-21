import sys

read = sys.stdin.readline

n, k = map(int, read().split())
ws = [list(map(int, read().split())) for _ in range(n)]
dp = [0] * (k + 1)
for w, v in ws:
    for i in range(len(dp)):
        if dp[i] and i + w < k + 1:
            dp[i+w] = max(dp[i+w], dp[i] + v)
    dp[w] = max(dp[w], v)

print(max(dp))
