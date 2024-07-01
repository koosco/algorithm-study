import sys

read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
res = 0

for i in range(n - 2):
    for j in range(n - 2):
        cur = 0
        for x in range(3):
            for y in range(3):
                if graph[i+x][j+y] == 1:
                    cur += 1
        res = max(res, cur)
print(res)
