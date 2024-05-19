import sys
from typing import List
read = sys.stdin.readline

'''
문자의 길이는 n
연속하여 같은 숫자가 3번 나오는 경우는 제외
'''

def sol(ret: List[int]=[]):
    if len(ret) == n:
        res.append(ret[:])
        return
    for num in nums:
        if len(ret) >= 2 and ret[-1] == num and ret[-2] == num:
            continue
        sol(ret + [num])
    
k, n = map(int, read().split())
res = []
nums: List[int] = [i for i in range(1, k+1)]
sol()

for elem in res:
    print(*elem)