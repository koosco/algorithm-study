import sys
from typing import List
from math import ceil, log2

read = sys.stdin.readline

n, m, k = map(int, read().split())
s = 2 ** ceil(log2(n))
tree = [0] * (s * 2)

for i in range(n):
    tree[s + i] = int(read())

for i in range(s - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

queries: List[List[int]] = [list(map(int, read().split())) for _ in range(m + k)]


def get_sum(l_idx: int, r_idx: int) -> int:
    l_idx += s
    r_idx += s

    ret = 0

    while l_idx <= r_idx:
        if l_idx & 1:
            ret += tree[l_idx]
            l_idx += 1
        if not r_idx & 1:
            ret += tree[r_idx]
            r_idx -= 1
        l_idx >>= 1
        r_idx >>= 1
    return ret


def update(idx: int, value: int):
    idx += s
    tree[idx] = value
    while idx > 1:
        idx >>= 1
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


for q in queries:
    match q[0]:
        case 1:
            update(q[1] - 1, q[2])
        case 2:
            print(get_sum(q[1] - 1, q[2] - 1))
