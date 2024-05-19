def f(n):
    a = [1, 1, 2, 3, 2, 1, 4, 1, 1, 1, 2, 4, 2, 3, 4]
    idx = 0    
    
    while n < 15:
        n += a[n]
        idx += 1
    return idx

res = 0
for i in range(14):
    if f(i) == 5:
        res += 1
print(res)