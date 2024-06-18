n, x = map(int, input().split())
print(*[y for y in list(map(int, input().split())) if y < x])