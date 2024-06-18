x, y = map(int, [input() for _ in range(2)])
print((1 if y > 0 else 4) if x > 0 else (2 if y > 0 else 3))