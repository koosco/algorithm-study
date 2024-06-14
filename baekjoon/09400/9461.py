import sys
read = sys.stdin.readline

dp = [1, 1, 1] + [0] * 97
res = []

for i in range(3, 100):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(int(read())):
    res.append(str(dp[int(read()) - 1]))

print('\n'.join(res))