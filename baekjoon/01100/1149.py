import sys
read = sys.stdin.readline
MAX_SIZE = sys.maxsize

costs = [[MAX_SIZE] * 3]
dp = [[0] * 3 for _ in range(1001)]
n = int(read())
for _ in range(n):
    costs.append(list(map(int, read().split())))

dp[1] = costs[1]

for i in range(2, n + 1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[n]))