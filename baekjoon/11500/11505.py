import sys
from typing import List
from math import ceil, log2

read = sys.stdin.readline

n, m, k = map(int, read().split())
s = 2 ** ceil(log2(n))
tree: List[int] = [1] * s * 2
MOD = 1_000_000_007
res: List[str] = []

for i in range(n):
    tree[s + i] = int(read())

for i in range(s - 1, 0, -1):
    tree[i] = tree[i * 2] * tree[i * 2 + 1] % MOD


def get_mul(l_idx: int, r_idx: int):
    l_idx += s
    r_idx += s

    ret = 1

    while l_idx <= r_idx:
        if l_idx & 1:
            ret = ret * tree[l_idx] % MOD
            l_idx += 1
        if not r_idx & 1:
            ret = ret * tree[r_idx] % MOD
            r_idx -= 1
        l_idx >>= 1
        r_idx >>= 1

    return ret


def update(idx: int, value: int):
    idx += s
    tree[idx] = value
    while idx > 1:
        idx >>= 1
        tree[idx] = (tree[idx * 2] * tree[idx * 2 + 1]) % MOD


for _ in range(m + k):
    command, x, y = map(int, read().split())
    match command:
        case 1:
            update(x - 1, y)
        case 2:
            print(get_mul(x - 1, y - 1))
