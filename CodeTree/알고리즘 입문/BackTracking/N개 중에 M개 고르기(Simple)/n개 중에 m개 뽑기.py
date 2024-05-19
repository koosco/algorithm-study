from typing import List


def sol(idx: int, path: List[int]):
    if len(path) == m:
        res.append(path[:])
        return
    for i in range(idx, n+1):
        sol(i + 1, path + [i])

n, m = map(int, input().split())
res = []
sol(1, [])
for elem in res:
    print(*elem)