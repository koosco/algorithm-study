import sys
read = sys.stdin.readline

dp = [[0] * 15 for _ in range(15)]
first_row = [i for i in range(15)]
dp[0] = first_row
res = []

for i in range(1, 15):
    for j in range(15):
        if j == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]


for _ in range(int(read())):
    k, n = int(read()), int(read())
    res.append(str(dp[k][n]))

print('\n'.join(res))