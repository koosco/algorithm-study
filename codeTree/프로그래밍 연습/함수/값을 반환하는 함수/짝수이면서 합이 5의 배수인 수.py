n = input()
i_n = int(n)
if not i_n&1 and sum(map(int, list(n))) % 5 == 0:
    print('Yes')
else:
    print('No')