import sys
read = sys.stdin.readline

nums = [int(read()) for _ in range(9)]
max_v = max(nums)
argmax_v = nums.index(max(nums))
print(max_v, argmax_v+1)