import sys
from typing import List, Tuple
from heapq import *

read = sys.stdin.readline
INF = int(1e9)


def sol(start_v: int):
    q: List[Tuple[int, int]] = []
    path = {start_v}
    ret: int = 0
    heappush(q, (0, start_v))

    while q:
        dist, now = heappop(q)
        if costs[now] < dist:
            continue
        for node in graph[now]:
            path.add(node[0])
            cost = dist + node[1]
            if cost < costs[node[0]]:
                costs[node[0]] = cost
                heappush(q, (cost, node[0]))
    for cost in costs:
        if cost != INF:
            ret = max(ret, cost)
    return len(path), ret


for T in range(int(read())):
    n, d, c = map(int, read().split())
    graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    costs: List[int] = [INF] * (n + 1)

    for _ in range(d):
        u, v, w = map(int, read().split())
        graph[v].append((u, w))
    print(*sol(c))
