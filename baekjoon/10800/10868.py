import sys
from math import ceil, log2
from typing import List

INF = sys.maxsize
read = sys.stdin.readline

n, m = map(int, read().split())
s = 2 ** ceil(log2(n))
tree: List[int] = [INF] * s * 2


def query(l_idx: int, r_idx: int):
    l_idx += s
    r_idx += s

    min_v = INF

    while l_idx <= r_idx:
        if l_idx % 2:
            min_v = min(min_v, tree[l_idx])
            l_idx += 1
        if not r_idx % 2:
            min_v = min(min_v, tree[r_idx])
            r_idx -= 1
        l_idx //= 2
        r_idx //= 2

    print(min_v)


for i in range(n):
    tree[s + i] = int(read())

for i in range(s - 1, 0, -1):
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])

for i in range(m):
    l, r = map(int, read().split())
    query(l - 1, r - 1)