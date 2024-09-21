import sys
from itertools import combinations
from functools import reduce

read = sys.stdin.readline


def to_bit(song: str):
    res = 0
    for i in range(len(song)):
        if song[i] == 'Y':
            res |= (1 << i)
    return res


def sol():
    for i in range(1, n + 1):
        for comb in combinations(infos, i):
            base = 0
            for k in comb:
                base |= k
            if base == target:
                return i


n, m = map(int, read().split())
infos = [read().split() for _ in range(n)]
infos = [to_bit(infos[i][1]) for i in range(n)]
target = reduce(lambda a, b: a | b, infos, 0)
print(sol() if target else -1)