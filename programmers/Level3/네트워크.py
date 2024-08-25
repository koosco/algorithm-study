from collections import deque


def solution(n, computers):
    def sol(x: int):
        q = deque([x])
        while q:
            y = q.popleft()
            for v in graph[y]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True

    visited = [False] * n
    graph = {i: [] for i in range(n)}
    res = 0

    for i, computer in enumerate(computers):
        for j, friend in enumerate(computer):
            if i != j and friend:
                graph[i].append(j)
    print(graph)

    for computer_idx in range(n):
        if not visited[computer_idx]:
            sol(computer_idx)
            res += 1
    return res