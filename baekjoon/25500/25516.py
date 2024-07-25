import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def dfs(v=0, depth=0):
    global res
    if depth > k:
        return
    if apples[v]:
        res += 1
    for w in graph[v]:
        dfs(w, depth + 1)


n, k = map(int, read().split())
graph = {i: [] for i in range(n)}
res = 0

for _ in range(n - 1):
    a, b = map(int, read().split())
    graph[a].append(b)
apples = list(map(int, read().split()))
dfs()
print(res)