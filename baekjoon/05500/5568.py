from typing import List


def dfs(remainder: List[str], path: List[str], depth: int):
    if depth == k:
        x = int(''.join(path))
        res.add(x)
        return
    for num in remainder:
        next = remainder[:]
        next.remove(num)
        dfs(next, path + [num], depth + 1)


n, k = int(input()), int(input())
cards = [input() for _ in range(n)]
res = set()
dfs(cards, [], 0)
print(len(res))