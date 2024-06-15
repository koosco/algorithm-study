import sys
read = sys.stdin.readline

dynamic_list = []
res = []
for _ in range(int(read())):
    command = list(read().split())
    if command[0] == 'push_back':
        dynamic_list.append(command[1])
    elif command[0] == 'pop_back':
        dynamic_list.pop()
    elif command[0] == 'size':
        res.append(str(len(dynamic_list)))
    elif command[0] == 'get':
        res.append(dynamic_list[int(command[1])-1])

print('\n'.join(res))