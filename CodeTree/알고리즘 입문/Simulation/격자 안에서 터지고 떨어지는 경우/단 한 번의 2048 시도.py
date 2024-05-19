import sys
from typing import List
read = sys.stdin.readline

def sol():
    graph = [list(map(int, read().split())) for _ in range(4)]
    dir = read().rstrip()
    
    if dir == 'L':
        for i in range(4):
            tmp = []
            for j in range(4):
                add(i, j, tmp)
            fill(tmp)
            graph[i] = tmp
    
    elif dir == 'R':
        for i in range(4):
            tmp = []
            for j in range(3, -1, -1):
                add(i, j, tmp)
            fill(tmp)
            graph[i] = reversed(tmp)
    
    elif dir == 'U':
        for j in range(4):
            tmp = []
            for i in range(4):
                add(i, j, tmp)
            fill(tmp)
            for i in range(4):
                graph[i][j] = tmp[i][j]
                
    def add(i: int, j: int, nums: List[int]):
        if nums and nums[-1] == graph[i][j]:
            nums[-1] *= 2
        elif graph[i][j] != 0:
            nums.append(graph[i][j])
    
    def fill(nums: List[int]):
        while len(nums) < 4:
            tmp.append(0)
        pass
            
    
    for row  in graph:
        print(*row)
        print()


sol()