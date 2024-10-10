import sys
from heapq import *
from typing import Tuple, List

read = sys.stdin.readline
INF = int(1e9)
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def get_min_distance():
    costs: List[List[int]] = [[INF] * n for _ in range(n)]
    q: List[Tuple[int, Tuple[int, int]]] = []
    heappush(q, (graph[0][0], (0, 0)))
    costs[0][0] = graph[0][0]

    while q:
        dist, now = heappop(q)
        y, x = now
        if costs[y][x] < dist:
            continue

        for d in directions:
            ny, nx = y + d[0], x + d[1]
            if 0 <= ny < n and 0 <= nx < n:
                cost = dist + graph[ny][nx]
                if cost < costs[ny][nx]:
                    costs[ny][nx] = cost
                    heappush(q, (cost, (ny, nx)))
    return costs[-1][-1]


def sout(x: int):
    print(f'Problem {idx}: {x}')


idx = 1
while True:
    n = int(read())
    if not n:
        break
    graph = [list(map(int, read().split())) for _ in range(n)]
    sout(get_min_distance())
    idx += 1
