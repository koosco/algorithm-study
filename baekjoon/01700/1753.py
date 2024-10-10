import sys
from typing import List, Tuple
from heapq import *

read: callable = sys.stdin.readline
INF = int(1e9)


def dijkstra(start_v: int):
    q: List[Tuple[int, int]] = []
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


v, e = map(int, read().split())
k = int(read())

graph: List[List[Tuple[int, int]]] = [[] for _ in range(v + 1)]
costs: List[int] = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

dijkstra(k)
for cost in costs[1:]:
    print(cost if cost != INF else 'INF')
