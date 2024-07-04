from collections import defaultdict

a, p = map(int, input().split())
D = defaultdict(int)
D[a] += 1
res = 0

while True:
    x = sum(map(lambda x: x ** p, map(int, list(str(a)))))
    if D[x] + 1 == 3:
        break
    D[x] += 1
    a = x
for _, cnt in D.items():
    if cnt == 1:
        res += 1
print(res)