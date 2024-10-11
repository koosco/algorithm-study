import sys
from heapq import *
from typing import Tuple, List

read = sys.stdin.readline
INF = int(1e9)


def sol(start_v: int):
    q: List[Tuple[int, int]] = []
    costs: List[int] = [INF] * (n + 1)
    heappush(q, (0, start_v))
    costs[start_v] = 0

    while q:
        dist, now = heappop(q)
        if costs[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < costs[node[0]]:
                costs[node[0]] = cost
                heappush(q, (cost, node[0]))
    return costs


for T in range(int(read())):
    n, m, t = map(int, read().split())
    s, g, h = map(int, read().split())
    graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, read().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    ts = [int(read()) for _ in range(t)]
    res = []

    ds = sol(s)
    dg = sol(g)
    dh = sol(h)

    for e in ts:
        if ds[g] + dg[h] + dh[e] == ds[e] or ds[h] + dh[g] + dg[e] == ds[e]:
            res.append(e)
    print(*sorted(res))
