import sys
read = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, r, c = map(int, read().split())
r, c = r - 1, c - 1
graph = [list(map(int, read().split())) for _ in range(n)]
res = []

while True:
    res.append(graph[r][c])
    flag = False
    for d in directions:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < n and 0 <= nc < n and \
            graph[nr][nc] > graph[r][c]:
                r, c = nr, nc
                flag = True
                break
    if not flag:
        break
    
print(*res)