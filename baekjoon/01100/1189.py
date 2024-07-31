def sol(i, j):
    if visited[0][c - 1] == k:
        global res
        res += 1
        return
    if visited[i][j] >= k:
        return
    for d in directions:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < r and 0 <= nj < c and not visited[ni][nj] and \
                not graph[ni][nj]:
            visited[ni][nj] = visited[i][j] + 1
            sol(ni, nj)
            visited[ni][nj] = 0


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

r, c, k = map(int, input().split())
graph = [list(map(lambda x: {'.': 0, 'T': 1}[x], list(input()))) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
visited[r-1][0], res = 1, 0
sol(r-1, 0)
print(res)