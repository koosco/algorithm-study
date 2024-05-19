def sol(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        c = a % b
        a, b = b, c
    print(a)
n, m = map(int, input().split())
sol(n, m)