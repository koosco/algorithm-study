n = int(input())
nums = list(map(int, input().split()))
cur = max_v = 0

if max(nums) < 0:
    print(max(nums))
else:
    for i in range(n):
        cur += nums[i]
        if cur < 0:
            cur = 0
        if max_v < cur:
            max_v = cur
    print(max_v)