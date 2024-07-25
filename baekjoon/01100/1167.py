import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def dfs(s, v, visited):
    for w in graph[v]:
        if not visited[w[0]]:
            visited[w[0]] = s + w[1]
            dfs(s + w[1], w[0], visited)


n = int(read())
graph = {i: [] for i in range(1, n + 1)}
visited_for_first_node = [0] * (n + 1)
visited_for_second_node = [0] * (n + 1)

for _ in range(n):
    nums = list(map(int, read().split()))
    w = nums[0]
    info = nums[1:-1]
    for i in range(0, len(info), 2):
        graph[w].append((info[i], info[i + 1]))
start_v = list(graph.keys())[0]
visited_for_first_node[start_v] = -1
dfs(0, start_v, visited_for_first_node)
first_node = visited_for_first_node.index(max(visited_for_first_node))
visited_for_second_node[first_node] = -1
dfs(0, first_node, visited_for_second_node)
print(max(visited_for_second_node))

# floyd-warshall : memory 초과
# v = int(read())
# graph = [[INF] * v for _ in range(v)]
# res = -INF
#
# for _ in range(v):
#     nums = list(map(int, read().split()))
#     w = nums[0]
#     info = nums[1:-1]
#     for i in range(0, len(info), 2):
#         graph[w-1][info[i]-1] = info[i+1]
# for i in range(v):
#     graph[i][i] = 0
#
# for k in range(v):
#     for i in range(v):
#         for j in range(v):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#             if graph[i][j] != INF:
#                 res = max(res, graph[i][j])
# print(res)
