from typing import List


def sol(candidates: List[int], path: List[int]):
    if len(path) == n:
        res.append(path[:])
    for num in candidates:
        next_nums = []
        for next_num in candidates:
            if next_num == num:
                continue
            next_nums.append(next_num)
        sol(next_nums, path + [num])

n = int(input())
res = []
sol(list(range(1, n+1)), [])

for elem in res:
    print(*elem)