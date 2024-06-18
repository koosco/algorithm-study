import sys
read = sys.stdin.readline

stk = []
nums = [int(read()) for _ in range(int(read()))]
for num in nums:
    if num == 0:
        stk.pop()
    else:
        stk.append(num)
print(sum(stk))