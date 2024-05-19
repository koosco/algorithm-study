import sys
read = sys.stdin.readline

def crush_check():
    if r == n - 1:
        return True
    for i in range(m):
        if graph[r+1][k+i] == 1:
            return True
    return False

def fill():
    for i in range(m):
        graph[r][k+i] = 1

n, m, k = map(int, read().split())
r = 0
k -= 1
graph = [list(map(int, read().split())) for _ in range(n)]

while not crush_check():
    r += 1
fill()
for row in graph:
    print(*row)