def f(n):
    s = 0
    for i in range(0, n, 2):
        for j in range(0, i, 2):
            s += i + j
    return s

'''
s = 2
i = 0
i = 2
    j = 0 : s = 2
i = 4
    j = 0 : s = 6
    j = 2 : s = 12
i = 6
    j = 0 : s = 18
    j = 2 : s = 26
    j = 4 : s = 36
i = 8
    j = 0 : s = 44
    j = 2 : s = 54
    j = 4 : s = 66
    j = 6 : s = 80
'''