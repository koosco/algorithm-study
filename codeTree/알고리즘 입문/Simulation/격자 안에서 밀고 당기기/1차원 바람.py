import sys
from typing import List, Tuple
from collections import deque
read = sys.stdin.readline

LEFT = True
RIGHT = False
UP = True
DOWN = False

def sol():
    def lozic(idx: int, lr: bool, ud: bool=None):
        queue = deque()
        queue.append((idx, lr, ud))
        
        while queue:
            _idx, _lr, _ud = queue.popleft()
            wind_blow(_idx, _lr)

            nlr = LEFT if _lr is RIGHT else RIGHT
            if _ud is None:
                if is_possible(_idx, _idx - 1):
                    queue.append((_idx - 1, nlr, DOWN))
                if is_possible(_idx, _idx + 1):
                    queue.append((_idx + 1, nlr, UP))
            elif _ud is DOWN and is_possible(_idx, _idx - 1):
                queue.append((_idx - 1, nlr, DOWN))
            elif _ud is UP and is_possible(_idx, _idx + 1):
                queue.append((_idx + 1, nlr, UP))
                
    def is_possible(current_idx: int, next_idx: int) -> bool:
        if 0 <= next_idx < n:
            for i in range(m):
                if graph[current_idx][i] == graph[next_idx][i]:
                    return True
        return False

    def wind_blow(row_idx: int, direction: bool):
        if direction == RIGHT:
            graph[row_idx] = graph[row_idx][1:] + [graph[row_idx][0]]
            
        elif direction == LEFT:
            graph[row_idx] = [graph[row_idx][-1]] + graph[row_idx][:-1]
            
    n, m, q = map(int, read().split())
    graph = [list(map(int, read().split()))
                for _ in range(n)]
    winds = []
    for _ in range(q):
        r, d = read().split()
        _r = int(r) - 1
        _d = LEFT if d == 'L' else RIGHT
        winds.append((_r, _d))
        
    for wind in winds:
        lozic(wind[0], wind[1])
        
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=' ')
        print()

sol()