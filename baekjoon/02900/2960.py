def sol(i: int):
    global cnt, k, res
    j = 1
    while i * j <= n:
        if nums[i * j]:
            nums[i * j] = False
            cnt += 1
            if cnt == k:
                res = i * j
        j += 1


n, k = map(int, input().split())
nums = [True] * (n + 1)
res, cnt = None, 0

for i in range(2, n + 1):
    if nums[i]:
        sol(i)
    if res is not None:
        break
print(res)
