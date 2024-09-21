n = sorted(list(map(int, list(input()))), reverse=True)
print(''.join(map(str, n)) if not (n[-1] or sum(n) % 3) else -1)
