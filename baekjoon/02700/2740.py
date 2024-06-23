import sys

read = sys.stdin.readline

n, m = map(int, read().split())
A = [list(map(int, read().split())) for _ in range(n)]
_, k = map(int, read().split())
B = [list(map(int, read().split())) for _ in range(m)]
res = [[0] * k for _ in range(n)]

for a in range(n):
    for b in range(k):
        for c in range(m):
            res[a][b] += A[a][c] * B[c][b]
for row in res:
    print(*row)
