res = [True] * 10_001
for i in range(1, 10_001):
    num = sum(map(int, list(str(i)))) + i
    if num <= 10_000:
        res[num] = False
print('\n'.join([str(i) for i in range(1, 10_001) if res[i]]))