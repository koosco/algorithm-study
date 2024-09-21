stick = input()
l = len(stick)
res, i, stk = 0, 0, 0

while i < l:
    if stick[i] == '(':
        if stick[i+1] == ')':
            i += 2
            res += stk
        else:
            stk += 1
            res += 1
            i += 1
    else:
        stk -= 1
        i += 1
print(res)