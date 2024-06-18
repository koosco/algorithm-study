import sys
read = sys.stdin.readline

for i in range(1, int(read())+1):
    print(f'Case #{i}:', sum(map(int, read().split())))