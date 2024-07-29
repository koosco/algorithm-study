import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(p: int, v: int = 1):
    res[v] = p
    for w in graph[v]:
        if not res[w]:
            dfs(v, w)

n = int(read())
res = [0] * (n + 1)
res[1] = -1
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)
dfs(1)
print(*res[2:], sep='\n')
