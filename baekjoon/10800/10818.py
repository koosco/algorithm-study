_ = int(input())
nums = list(map(int, input().split()))
v = int(1e6)
min_v, max_v = v, -v
for num in nums:
    if min_v > num:
        min_v = num
    if max_v < num:
        max_v = num
print(min_v, max_v)