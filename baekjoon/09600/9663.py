n = int(input())
graph = [[False] * n for _ in range(n)]
res = 0


def point(r_idx: int = 0):
    if r_idx >= n:
        global res
        res += 1
        return
    for c_idx in range(n):
        if not graph[r_idx][c_idx]:
            painted = paint(r_idx, c_idx)
            point(r_idx + 1)
            remove(painted)


def remove(points):
    for x, y in points:
        graph[x][y] = False


def paint(x: int, y: int):
    ret = []
    directions = [(1, -1), (1, 0), (1, 1)]
    for size in range(n - x):
        for direction in directions:
            nx, ny = x + direction[0] * size, y + direction[1] * size
            if 0 <= nx < n and 0 <= ny < n:
                if not graph[nx][ny]:
                    graph[nx][ny] = True
                    ret.append((nx, ny))
    return ret

point()
print(res)
