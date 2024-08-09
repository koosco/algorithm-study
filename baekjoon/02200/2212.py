import sys

read = sys.stdin.readline

n, k = int(read()), int(read())
ps = sorted(list(map(int, read().split())))
print(sum(sorted([ps[i] - ps[i-1] for i in range(1, n)])[:n-k]))