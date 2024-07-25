import sys

read = sys.stdin.readline

sys.setrecursionlimit(int(1e9))


def dfs(v):
    global res
    if not graph[v]:
        res += 1
        return
    elif del_v in graph[v] and len(graph[v]) == 1:
        res += 1
        return
    for w in graph[v]:
        if w != del_v:
            dfs(w)


n = int(read())
trees = list(map(int, read().split()))
del_v = int(read())
graph = {i: [] for i in range(n)}
start_v = None
res = 0

for i in range(len(trees)):
    if trees[i] == -1:
        start_v = i
        continue
    graph[trees[i]].append(i)
if start_v != del_v:
    dfs(start_v)
print(res)
