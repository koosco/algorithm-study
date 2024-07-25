import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def sol

n, m = map(int, read().split())
relations = {i: [] for i in range(n)}

for _ in range(m):
    s, e = map(int, read().split())
    relations[s].append(e)
    relations[e].append(s)

