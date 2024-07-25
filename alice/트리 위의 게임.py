import sys
from typing import List

read = sys.stdin.readline


def sol(v: int, child_score: List[int]):
    bx, by = child_score
    scores[v] = max(scores[v], [by + v, bx], key=lambda x: (x[0], -x[1]))
    for w in parent[v]:
        sol(w, scores[v])


n = int(read())
graph = {i: [] for i in range(1, n + 1)}
parent = {i: [] for i in range(1, n + 1)}
scores = [[0] * 2 for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, read().split())
    graph[s].append(e)
    parent[e].append(s)

for k in graph:
    if not graph[k]:
        print('k is', k)
        scores[k] = [k, 0]
        for p in parent[k]:
            sol(p, scores[k])
print(graph)
print(parent)
print(scores)
for f, s in scores[1:]:
    print(1 if f >= s else 0)
