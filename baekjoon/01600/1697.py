from collections import deque

n, k = map(int, input().split())
visited = [0] * 100_001
visited[n] = 1
q = deque([n])
while not visited[k]:
    x = q.popleft()
    if x * 2 < 100_001 and not visited[2*x]:
        visited[2*x] = visited[x] + 1
        q.append(2*x)
    if -1 < x - 1 and not visited[x-1]:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    if x + 1 < 100_001 and not visited[x+1]:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
print(visited[k]-1)