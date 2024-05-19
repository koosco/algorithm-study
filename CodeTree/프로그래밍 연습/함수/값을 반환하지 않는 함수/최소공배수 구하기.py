def sol(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        c = a % b
        a, b = b, c
    return a

n, m = map(int, input().split())
min_v = sol(n, m)
print(n * m // min_v)