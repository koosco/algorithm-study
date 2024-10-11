import sys
from typing import List
from collections import deque

read: callable = sys.stdin.readline

for T in range(int(read())):
    n, k = map(int, read().split())
    ds: List[int] = [0] + list(map(int, read().split()))
    graph: List[List[int]] = [[] for _ in range(n + 1)]
    degree: List[int] = [0] * (n + 1)
    dp: List[int] = [0] * (n + 1)
    q = deque()

    for _ in range(k):
        x, y = map(int, read().split())
        graph[x].append(y)
        degree[y] += 1
    w = int(read())

    for i in range(1, n + 1):
        if not degree[i]:
            q.append(i)
            dp[i] = ds[i]
    while q:
        x = q.popleft()
        for next_node in graph[x]:
            degree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[x] + ds[next_node])
            if not degree[next_node]:
                q.append(next_node)
    print(dp[w])
