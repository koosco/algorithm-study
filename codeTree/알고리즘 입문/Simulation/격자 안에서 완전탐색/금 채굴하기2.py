import sys

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]


def count_gold(row, col, k):
    gold = 0
    directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    x, y = row - k, col
    for direction in directions:
        for _ in range(k):
            nx, ny = x + direction[0], y + direction[1]
            if 0 <= nx < n and 0 <= ny < n:
                gold += graph[nx][ny]
            x, y = nx, ny
    return gold


def cost(k):
    return k ** 2 + (k + 1) ** 2


def sol():
    max_gold = 0
    for i in range(n):
        for j in range(n):
            gold = graph[i][j]
            for k in range(2 * (n - 1) + 1):
                gold += count_gold(i, j, k)
                if cost(k) <= m * gold:
                    max_gold = max(max_gold, gold)
    return max_gold


print(sol())
