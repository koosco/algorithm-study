M = int(1e9)
def sol(num: int, depth: int, plus: int, minus: int, mul: int, div: int):
    if depth == n - 1:
        global min_v, max_v
        min_v = min(min_v, num)
        max_v = max(max_v, num)
        return
    if plus:
        sol(num + nums[depth+1], depth+1, plus-1, minus, mul, div)
    if minus:
        sol(num - nums[depth+1], depth+1, plus, minus-1, mul, div)
    if mul:
        sol(num * nums[depth+1], depth+1, plus, minus, mul-1, div)
    if div:
        sol(-(-num // nums[depth+1]) if num < 0 else num // nums[depth+1], depth+1, plus, minus, mul, div-1)



n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
min_v, max_v = M, -M
sol(nums[0], 0, op[0], op[1], op[2], op[3])
print(max_v, min_v, sep='\n')