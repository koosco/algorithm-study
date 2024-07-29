import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(v: int, depth: int = 0):
    if scores[v] == k:
        global res
        res = depth
    for w in tree[v]:
        dfs(w, depth + 1)


n, k = map(int, read().split())
tree = {i: [] for i in range(n)}
res = None
for _ in range(n - 1):
    p, c = map(int, read().split())
    tree[p].append(c)
scores = list(map(int, read().split()))
dfs(0)
print(res)