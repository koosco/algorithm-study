n, m = map(int, input().split())
mx, my = int(1e9), int(1e9)
res = 0

for _ in range(m):
    x, y = map(int, input().split())
    mx = min(mx, x)
    my = min(my, y)

if mx >= my * 6:
    res += my * n
else:
    p, n = divmod(n, 6)
    res += mx * p
    res += mx if mx < my * n else my * n
print(res)