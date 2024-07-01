def check(x: str):
    if sum(map(int, list(x))) % 3 == 0:
        return True
    for x_i in x:
        if x_i in ('3', '6', '9'):
            return True
    return False

a, b = map(int, input().split())
res = 0
for i in range(a, b + 1):
    if check(str(i)):
        res += 1
print(res)