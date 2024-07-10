import sys
from collections import defaultdict
from typing import List

read = sys.stdin.readline


def sol(L: List[int], i=0):
    if len(L) == 1:
        res_dict[i].append(L[0])
        return
    mid = len(L) // 2
    res_dict[i].append(L[mid])
    sol(L[:mid], i + 1)
    sol(L[mid+1:], i + 1)


k = int(read())
res_dict = defaultdict(list)
sol(list(map(int, read().split())))
for _, v in res_dict.items():
    print(*v)