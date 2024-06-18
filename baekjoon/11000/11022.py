import sys

read = sys.stdin.readline

for i in range(int(read())):
    a, b = map(int, input().split())
    print(f'Case #{i + 1}:', a, '+', b, '=', a + b)
