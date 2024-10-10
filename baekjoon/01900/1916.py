import sys
from heapq import *
from typing import List, Tuple

read = sys.stdin.readline
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


n, m = int(read()), int(read())
graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
costs: List[int] = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))
a, b = map(int, read().split())

dijkstra(a)

print(costs[b])