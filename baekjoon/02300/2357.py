import sys
from typing import List
from math import ceil, log2

read = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, read().split())
s = 2 ** ceil(log2(n))
tree: List[List[int]] = [[INF, -INF]] * s * 2

for i in range(n):
    x = int(read())
    tree[s + i] = [x, x]

for i in range(s - 1, 0, -1):
    c1 = i * 2
    c2 = i * 2 + 1
    tree[i] = [min(tree[c1][0], tree[c2][0]), max(tree[c1][1], tree[c2][1])]


def query(l_idx: int, r_idx: int):
    l_idx += s
    r_idx += s

    min_v, max_v = INF, -INF

    while l_idx <= r_idx:
        if l_idx % 2:
            min_v = min(min_v, tree[l_idx][0])
            max_v = max(max_v, tree[l_idx][1])
            l_idx += 1
        if not r_idx % 2:
            min_v = min(min_v, tree[r_idx][0])
            max_v = max(max_v, tree[r_idx][1])
            r_idx -= 1
        l_idx //= 2
        r_idx //= 2

    print(min_v, max_v)


for _ in range(m):
    l, r = map(int, read().split())
    query(l - 1, r - 1)
