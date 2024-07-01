import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]

def get_area(k):
    return k ** 2 + (k+1) ** 2

def get_gold_count(row, col, k):
    return sum([
        graph[i][j]
        for i in range(n)
        for j in range(n)
        if abs(i-row) + abs(j-col) <= k
    ])

res = 0
for i in range(n):
    for j in range(n):
        for k in range(2*(n-1) + 1):
            gold = get_gold_count(i, j, k)

            if gold * m >= get_area(k):
                res = max(res, gold)
print(res)