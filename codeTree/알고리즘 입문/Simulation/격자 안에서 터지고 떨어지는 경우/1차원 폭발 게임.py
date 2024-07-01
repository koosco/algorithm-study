import sys
from typing import List
read = sys.stdin.readline      

def check():
    if not bombs:
        return False
    cur = bombs[0]
    cnt = 0
    for bomb in bombs:
        if bomb == cur:
            cnt += 1
            if cnt >= m:
                return True
        else:
            cur = bomb
            cnt = 1
    return False   

n, m = map(int, read().split())
bombs = [int(read()) for _ in range(n)]

while check():
    new_bombs = []
    prev = bombs[0]
    cnt = 0
    for i, bomb in enumerate(bombs):
        if bomb == prev:
            # 이전 값과 현재 값이 같은 경우
            cnt += 1
        else:
            # 이전 값과 현재 값이 다른 경우
            if cnt < m:
                # 여태까지 나온 횟수를 검사하여 요소 추가
                for _ in range(cnt):
                    new_bombs.append(prev)
            # 현재값 초기화
            prev = bomb
            cnt = 1
        # 만약 현재 cnt가 m보다 크면 생략
    if cnt < m:
        for _ in range(cnt):
            new_bombs.append(prev)
    bombs = new_bombs[:]
  
print(len(bombs))
for bomb in bombs:
    print(bomb)