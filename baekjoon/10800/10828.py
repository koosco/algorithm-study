import sys
read = sys.stdin.readline

stk, res = [], []
for _ in range(int(read())):
    c = read().split()
    if c[0] == 'push':
        stk.append(c[1])
    elif c[0] == 'pop':
        res.append(stk.pop() if stk else -1)
    elif c[0] == 'size':
        res.append(len(stk))
    elif c[0] == 'empty':
        res.append(1 if not stk else 0)
    elif c[0] == 'top':
        res.append(stk[-1] if stk else -1)
print('\n'.join(map(str, res)))