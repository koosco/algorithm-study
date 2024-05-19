import sys
read = sys.stdin.readline

def sol():
    def bomb(x: int, y: int, mag: int):
        for i in range(-mag, mag+1):
            if 0 <= x + i < n:
                graph[x+i][y] = -1
            if 0 <= y + i < n:
                graph[x][y+i] = -1
        gravity()
                
    def gravity():
        for j in range(n):
            new_col = []
            for i in range(n-1, -1, -1):
                if graph[i][j] != -1:
                    new_col.append(graph[i][j])
            while len(new_col) < n:
                new_col.append(0)
            for i in range(n-1, -1, -1):
                graph[i][j] = new_col[n-1-i]
    
    n = int(read())
    graph = [list(map(int, read().split())) for _ in range(n)]
    r, c = map(lambda x: x-1, map(int, read().split()))
    bomb(r, c, graph[r][c]-1)
    for row in graph:
        print(*row)
sol()