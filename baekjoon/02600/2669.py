poses = [list(map(int, input().split())) for _ in range(4)]
graph = [[False] * 100 for _ in range(100)]

for x1, y1, x2, y2 in poses:
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = True

print(sum(map(sum, graph)))