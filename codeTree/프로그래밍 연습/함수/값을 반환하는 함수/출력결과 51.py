def Lee(x):
    trigger = 10
    while x:
        if x % 10 > trigger:
            return 0
        trigger = x % 10
        x /= 10
    return 1

print(Lee(654321) + Lee(123345) + Lee(442211) + Lee(202104))

'''
Lee(654321) + Lee(123345) + Lee(442211) + Lee(202104)
1) Lee(654321)
x = 654321
trigger = 10
trigger = 1
x = 

2) Lee(123345)
x = 123345
trigger = 10 -
'''