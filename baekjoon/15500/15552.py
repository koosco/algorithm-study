import sys
read = sys.stdin.readline

for _ in range(int(read())):
    a, b = map(int, read().split())
    print(a + b)