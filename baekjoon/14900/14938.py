import sys
from heapq import *
from typing import List, Tuple

read = sys.stdin.readline
INF = int(1e9)


def sol(start_v: int):
    costs: List[int] = [INF] * (n + 1)
    costs[start_v] = 0
    q: List[Tuple[int, int]] = []
    heappush(q, (0, start_v))

    while q:
        dist, now = heappop(q)
        if costs[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost <= m and cost < costs[node[0]]:
                costs[node[0]] = cost
                heappush(q, (cost, node[0]))

    return sum(ts[i] for i in range(1, n + 1)
               if costs[i] < INF)


n, m, r = map(int, read().split())
ts = [0] + list(map(int, read().split()))
graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
res = 0
for _ in range(r):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for i in range(1, n + 1):
    res = max(res, sol(i))
print(res)
