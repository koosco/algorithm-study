import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def sol(v: int, p: int = -1):
    print('v is', v, ', p is', p)
    visited.add(v)
    flag = False
    for w in graph[v]:
        if w not in visited:
            sol(w, v)
            if res[w]:
                res[v] = 1
                flag = True
    if flag:
        res[v] = 1


n = int(read())
graph = {i: [] for i in range(1, n + 1)}
res = [0] * (n + 1)
visited = set()
for _ in range(n - 1):
    s, e = map(int, read().split())
    graph[s].append(e)
print(graph)

for i in range(1, n+1):
    sol(i)
for r in res[1:]:
    print(r)
