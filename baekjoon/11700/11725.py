import sys
from typing import Dict, List
sys.setrecursionlimit(int(1e9))
read = sys.stdin.readline


def dfs(parent: int = 0, node: int = 1):
    if visited[node] != 0:
        return
    visited[node] = parent
    for child in tree[node]:
        if not visited[child]:
            dfs(node, child)


n: int = int(read())
tree: Dict[int, List[int]] = {i + 1: [] for i in range(n)}
visited: List[int] = [0] * (n + 1)

s: int
e: int
for _ in range(n - 1):
    s, e = map(int, read().split())
    tree[s].append(e)
    tree[e].append(s)

dfs()
print('\n'.join(map(str, visited[2:])))
