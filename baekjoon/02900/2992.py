from itertools import permutations

inputs = input()
num = sorted(list(map(int, list(inputs))))
for perm in permutations(num, len(num)):
    x = int(''.join(map(str, perm)))
    if x > int(inputs):
        print(x)
        break
else:
    print(0)
