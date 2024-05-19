from typing import List
from functools import reduce

def sol(idx: int, path: List[int]):
    if len(path) == m:
        res.append(path[:])
        return
    for i in range(idx, n):
        sol(i + 1, path + [nums[i]])
    

n, m = map(int, input().split())
nums = list(map(int, input().split()))
res = []
xor_res = 0
sol(0, [])
for elem in res:
    xor_res = max(xor_res, reduce(lambda x, y: x^y, elem))
print(xor_res)