import sys

sys.setrecursionlimit(int(1e6))
read = sys.stdin.readline


def dfs(v):
    global cnt
    visited[v] = cnt
    cnt += 1
    for e in graph[v]:
        if not visited[e]:
            dfs(e)


n, m, r = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    node.sort(reverse=True)

dfs(r)
print(*visited[1:], sep='\n')