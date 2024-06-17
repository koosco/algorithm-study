coins = (500, 100, 50, 10, 5, 1)
money = 1000 - int(input())
res = 0

for coin in coins:
    res += (money // coin)
    money %= coin
print(res)