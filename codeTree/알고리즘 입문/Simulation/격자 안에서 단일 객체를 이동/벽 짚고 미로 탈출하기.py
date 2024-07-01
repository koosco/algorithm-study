import sys
read = sys.stdin.readline

LEFT, RIGHT, DOWN, UP = (0, -1), (0, 1), (1, 0), (-1, 0)

def sol():
    def encounter():
        nonlocal dir
        if dir == LEFT:
            dir = DOWN
        elif dir == DOWN:
            dir = RIGHT
        elif dir == RIGHT:
            dir = UP
        elif dir == UP:
            dir = LEFT
            
    def check_wall():
        nonlocal dir
        if dir == LEFT and graph[x-1][y] == '#':
            return True
        elif dir == DOWN and graph[x][y-1] == '#':
            return True
        elif dir == RIGHT and graph[x+1][y] == '#':
            return True
        elif dir == UP and graph[x][y+1] == '#':
            return True
        return False

    def can_go():
        nonlocal dir
        nx, ny = x + dir[0], y + dir[1]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '#':
            return False
        return True

    def go():
        nonlocal dir, x, y, res
        x, y = x + dir[0], y + dir[1]
        res += 1

    def no_wall_change_dir():
        nonlocal dir
        if dir == LEFT:
            dir = UP
        elif dir == UP:
            dir = RIGHT
        elif dir == RIGHT:
            dir = DOWN
        elif dir == DOWN:
            dir = LEFT
            
    n = int(read())
    x, y = map(lambda a: a-1, map(int, read().split()))
    visited = set()
    graph = [list(read().rstrip()) for _ in range(n)]
    dir = RIGHT
    start = False
    res = 0
    
    while 0 <= x < n and 0 <= y < n:
        if (x, y, dir) in visited:
            print(-1)
            return
        else:
            visited.add((x, y, dir))
        if check_wall():
            if can_go():
                go()
            else:
                encounter()
        else:
            no_wall_change_dir()
            if can_go():
                go()
    print(res)
    
sol()