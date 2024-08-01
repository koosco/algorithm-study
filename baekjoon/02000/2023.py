from typing import List
import sys

read = sys.stdin.readline


def sol(path: List[str], depth: int = 1):
    if depth == n:
        res.append(''.join(path))
        return
    for k in range(10):
        tmp = int(''.join(path + [str(k)]))
        if is_prime(tmp):
            sol(path + [str(k)], depth + 1)


def is_prime(x: int):
    cnt = 0
    for j in range(1, int(x ** .5) + 1):
        if not x % j:
            cnt += 1
    return cnt == 1


n = int(input())
res = []
for i in range(2, 10):
    if is_prime(i):
        sol([str(i)])
print('\n'.join(res))