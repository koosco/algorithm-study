def calculate():
    ret = 0
    for horse in horses:
        if horse >= m:
            ret += 1
    return ret

def sol(turn: int):
    global res
    res = max(res, calculate())
    if turn >= n:
        return
    
    for i in range(k):
        if horses[i] >= m:
            continue
        horses[i] += nums[turn]
        sol(turn+1)
        horses[i] -= nums[turn]


n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
horses = [1] * k
res = 0

sol(0)
print(res)