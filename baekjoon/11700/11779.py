import sys
from heapq import *
from typing import List, Tuple

read = sys.stdin.readline
INF = int(1e9)


def sol(start_v: int):
    q = []
    heappush(q, (0, start_v))

    while q:
        dist, now = heappop(q)
        if costs[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < costs[node[0]]:
                costs[node[0]] = cost
                prev[node[0]] = now
                heappush(q, (cost, node[0]))


n, m = int(read()), int(read())
graph: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
costs = [INF] * (n + 1)
prev = [0] * (n + 1)

for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))
s, e = map(int, read().split())

sol(s)

path = [e]
now = e

while now != s:
    now = prev[now]
    path.append(now)
print(costs[e], len(path), end='\n')
print(*path[::-1])
