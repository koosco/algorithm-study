import sys
read = sys.stdin.readline

n = int(read())
cards = [0] + list(map(int, read().split()))
dp = [0] * 1001

for i in range(1, n+1):
    dp[i] = max(dp[i-1] + cards[1], cards[i])
print(dp)
print(dp[n])