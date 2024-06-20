import sys
from collections import deque

read = sys.stdin.readline

q = deque()
res = []
for _ in range(int(read())):
    command = read().split()
    if command[0] == 'push_front':
        q.appendleft(command[1])
    elif command[0] == 'push_back':
        q.append(command[1])
    elif command[0] == 'pop_front':
        res.append(q.popleft() if q else '-1')
    elif command[0] == 'pop_back':
        res.append(q.pop() if q else '-1')
    elif command[0] == 'size':
        res.append(str(len(q)))
    elif command[0] == 'empty':
        res.append('1' if not q else '0')
    elif command[0] == 'front':
        res.append(str(q[0]) if q else '-1')
    elif command[0] == 'back':
        res.append(str(q[-1]) if q else '-1')
print('\n'.join(res))