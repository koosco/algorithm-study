import sys
from typing import List, Tuple
from heapq import *

read = sys.stdin.readline
INF = int(1e9)


def dijkstra(start_v: int, target: int) -> int:
    costs: List[int] = [INF] * (n + 1)
    q = []
    heappush(q, (0, start_v))
    costs[start_v] = 0

    while q:
        dist, now = heappop(q)
        if costs[now] < dist:
            continue

        for node in graph[now]:
            cost: int = dist + node[1]
            if cost < costs[node[0]]:
                costs[node[0]] = cost
                heappush(q, (cost, node[0]))
    return costs[target]


def find_distance(target: int):
    ret: int = 0
    for i in range(1, n + 1):
        if i == target:
            continue
        ret = max(ret, dijkstra(i, target) + dijkstra(target, i))
    return ret


n, m, x = map(int, read().split())
graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

print(find_distance(x))
