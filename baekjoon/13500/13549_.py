from collections import deque
from typing import List

n, k = map(int, input().split())
costs: List[int] = [0] * 100_001

q = deque([n])
costs[n] = 1

while not costs[k]:
    x: int = q.popleft()
    if x * 2 < 100_001 and not costs[x * 2]:
        costs[x * 2] = costs[x]
        q.appendleft(x * 2)
    if x - 1 > -1 and not costs[x - 1]:
        costs[x - 1] = costs[x] + 1
        q.append(x - 1)
    if x + 1 < 100_001 and not costs[x + 1]:
        costs[x + 1] = costs[x] + 1
        q.append(x + 1)

print(costs[k] - 1)
