import sys
from typing import List
read = sys.stdin.readline

def sol(ret: List[int]=[]):
    if len(ret) == n:
        res.append(ret[:])
        return
    for num in nums:
        sol(ret + [num])

k, n = map(int, read().split())
nums = list(range(1, k+1))
res = []
sol()

for elem in res:
    print(*elem)