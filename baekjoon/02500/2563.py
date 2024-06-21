import sys

read = sys.stdin.readline

graph = [[False] * 100 for _ in range(100)]

for _ in range(int(read())):
    left_distance, lower_distance = map(int, read().split())
    for row_idx in range(lower_distance, lower_distance+10):
        for col_idx in range(left_distance, left_distance+10):
            graph[row_idx][col_idx] = True
print(sum(map(sum, graph)))