import sys
from typing import List

read = sys.stdin.readline


def get_pos(v: int):
    return (v // 5, v % 5)


def combinations(path: List[int], idx: int, k: int = 0):
    print(path)
    if len(path) == 7:
        print(path)
        global res
        res.append(path)
        return
    if idx == 25 or k > 4:
        return
    x, y = get_pos(idx)
    print(x, y)
    nk = k
    if not graph[x][y]:
        nk += 1
    combinations(path + [idx], idx + 1, nk)
    combinations(path, idx + 1, nk)


graph = [list(map(lambda x: {'Y': 0, 'S': 1}[x], list(read().rstrip()))) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
res = []
combinations([], 0)
print(res)
for row in graph:
    print(*row)
# for i in range(5):
#     for j in range(5):
#         sol(i, j)
