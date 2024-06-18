import sys
read = sys.stdin.readline

for _ in range(int(read())):
    print(sum(map(int, read().split())))