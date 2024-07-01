import sys
from collections import deque
read = sys.stdin.readline

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def sol():
    n, m, r, c = map(int, read().split())
    visited = set()
    r -=1; c -= 1
    q = deque()
    dist = 1
    t = 0
    res = 1
    q.append((r, c, dist))
    visited.add((r, c))
    
    while q:
        tmp = []
        t += 1
        for _ in range(len(q)):
            x, y, damage = q.popleft()
            tmp.append((x, y, damage * 2))
            for d in directions:
                nx, ny = x + damage * d[0], y + damage * d[1]
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) not in visited:
                        res += 1
                        visited.add((nx, ny))
                    tmp.append((nx, ny, damage * 2))
        for new_elem in tmp:
            q.append(new_elem)
        if t == m:
            break
    print(res)
sol()