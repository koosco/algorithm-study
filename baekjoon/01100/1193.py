x = int(input())
i = 1
while x - i > 0:
    x -= i
    i += 1

if i % 2 == 0:
    upper = 1
    lower = i
    for _ in range(x - 1):
        upper += 1
        lower -= 1
else:
    upper = i
    lower = 1
    for _ in range(x - 1):
        upper -= 1
        lower += 1
print(upper, lower, sep='/')
