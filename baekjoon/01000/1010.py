import sys
read = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]
res = []
for i in range(31):
    dp[i][0] = 1
    dp[i][i] = 1
    
for i in range(2, 31):
    for j in range(1, i+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for _ in range(int(read())):
    n, m = map(int, read().split())
    res.append(str(dp[m][n]))

print('\n'.join(res))