from typing import List

x = int(input())
if x < 10:
    print(x)
elif x >= 1023:
    print(-1)
else:
    def dfs(z: int, depth: int, k: int, path: List[str]):
        global cnt, flag, res
        if depth == k:
            cnt += 1
            if cnt == x:
                flag = True
                res = int(''.join(path))
                return
        for i in range(10):
            if i < z:
                dfs(i, depth + 1, k, path + [str(i)])
                if flag:
                    return


    cnt, res = 9, -1
    digit = 2
    flag = False
    while True:
        for y in range(1, 10):
            dfs(y, 1, digit, [str(y)])
            if flag:
                break
        digit += 1
        if flag:
            break
    print(res)