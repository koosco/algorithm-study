res = 0
cnt, decimal = 9, 1
n = int(input())
while n > 0:
    if n > cnt:
        res += cnt * decimal
    else:
        res += n * decimal
    n -= cnt
    cnt *= 10; decimal += 1

print(res)