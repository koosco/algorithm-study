import sys
from typing import List, Tuple
from heapq import *

read = sys.stdin.readline
INF = int(1e9)


def find_distance(start_v: int, target: int):
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

    return costs[target]


def sol():
    p1 = sum([find_distance(1, v1), find_distance(v1, v2), find_distance(v2, n)])
    p2 = sum([find_distance(1, v2), find_distance(v2, v1), find_distance(v1, n)])
    ret = p1 if p1 < p2 else p2
    return ret if ret < INF else -1


n, e = map(int, read().split())
graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, read().split())
print(sol())
