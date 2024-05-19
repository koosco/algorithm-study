import sys
from typing import List
read = sys.stdin.readline

def block1(i: int, j: int):
    sum_of_block = blocks[i][j] + blocks[i][j+1] + blocks[i+1][j] + \
                blocks[i+1][j+1]
    res = 0
    for x in range(2):
        for y in range(2):
            res = max(res, sum_of_block - blocks[i+x][j+y])
    return res

def block2(i: int, j: int):
    return blocks[i][j] + blocks[i+1][j] + blocks[i+2][j]

def block3(i: int, j: int):
    return blocks[i][j] + blocks[i][j+1] + blocks[i][j+2]

n, m = map(int, read().split())
blocks = [list(map(int, read().split())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(m):
        if i + 1 < n and j + 1 < m:
            res = max(res, block1(i, j))
        if i + 2 < n:
            res = max(res, block2(i, j))
        if j + 2 < m:
            res = max(res, block3(i, j))
print(res)