_list = [[2, 0, 1, 5],
         [0, 4, 1, 1],
         [1, 4, 0, 0]]

def f(b):
    for i in range(4):
        _list[b][i] = _list[(b + 1) % 3][(i + 1) % 4]
    # b = 1
    # list[1][0] = list[2][1]
    # list[1][1] = list[2][2]
    # list[1][2] = list[2][3]
    # list[1][3] = list[2][0]

'''
0 0 1 4
4 0 0 1
0 1 5 2
'''

f(1)
f(2)
f(0)
result = 0

for i in range(3):
    result += _list[i][(i + 1) % 4]
    # list[0][1] = 0
    # list[1][2] = 0
    # list[2][3] = 2
print(result)