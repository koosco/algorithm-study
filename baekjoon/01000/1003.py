import sys
read = sys.stdin.readline

dp = [0, 1, 1] + [0] * 38
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]
res = []

for _ in range(int(read())):
    N = int(read())
    if N == 0:
        res.append(('1', '0'))
    else:
        res.append((str(dp[N-1]), str(dp[N])))

for elem in res:
    print(' '.join(elem))