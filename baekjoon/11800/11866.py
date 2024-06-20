from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
res = []

while n:
    q.rotate(-k+1)
    res.append(str(q.popleft()))
    n -= 1
print('<', ', '.join(res), '>', sep='')