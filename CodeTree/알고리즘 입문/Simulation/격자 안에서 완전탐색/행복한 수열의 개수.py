import sys
from typing import List
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
res = 0

def sol(nums: List[int]):
    tmp = -1
    for elem in nums:
        if elem == tmp:
            cnt += 1
        else:
            tmp = elem
            cnt = 1
        if cnt >= m:
                return True

for row in graph:
    if sol(row):
        res += 1
        
for i in range(n):
    if sol([row[i] for row in graph]):
        res += 1

print(res)