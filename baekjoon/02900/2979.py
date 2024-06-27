import sys

read = sys.stdin.readline

a, b, c = map(int, read().split())
time = [0] * 101
res = 0

for _ in range(3):
    s, e = map(int, read().split())
    for t in range(s, e):
        time[t] += 1

for t in time:
    if t == 1:
        res += a
    elif t == 2:
        res += (2 * b)
    elif t == 3:
        res += (3 * c)

print(res)