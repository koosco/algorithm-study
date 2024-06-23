from collections import deque

q = deque(list(range(1, int(input()) + 1)))
res = []
while q:
    res.append(q.popleft())
    q.rotate(-1)
print(*res)