import sys

read = sys.stdin.readline
write = sys.stdout.write

s = set()
for _ in range(int(read())):
    command = read().split()
    if command[0] == 'add':
        s.add(int(command[1]))
    elif command[0] == 'remove':
        s.discard(int(command[1]))
    elif command[0] == 'check':
        write('1\n' if int(command[1]) in s else '0\n')
    elif command[0] == 'toggle':
        s.add(int(command[1])) if int(command[1]) not in s else s.discard(int(command[1]))
    elif command[0] == 'all':
        s = set(range(1, 21))
    elif command[0] == 'empty':
        s.clear()
