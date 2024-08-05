import sys
from typing import List

read = sys.stdin.readline


def sol(s: int = 1, b: int = 0, idx: int = 0, cnt: int = 0):
    if idx == n:
        if not cnt:
            return
        global res
        res = min(res, abs(s - b))
        return

    sol(s * ingredients[idx][0], b + ingredients[idx][1], idx + 1, cnt + 1)
    sol(s, b, idx + 1, cnt)


n = int(read())
ingredients = [list(map(int, read().split())) for _ in range(n)]
res = sys.maxsize
sol()
print(res)
