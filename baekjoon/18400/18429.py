import sys
from typing import List

sys.setrecursionlimit(int(1e9))


def sol(remainder: List[int], w: int = 500):
    if len(remainder) == 0:
        global res
        res += 1
        return
    for kit in remainder:
        n_w = w - k + kit
        if n_w >= 500:
            next = remainder[:]
            next.remove(kit)
            sol(next, n_w)

n, k = map(int, input().split())
res = 0
sol(list(map(int, input().split())))
print(res)