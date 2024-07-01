def sol(x: int):
    global b
    cnt = 2
    while x * cnt <= b:
        graph[x * cnt] = False
        cnt += 1

a, b = map(int, input().split())
if b <= 1:
    print(0)
else:
    graph = [True] * (b + 1)
    res = 0
    for i in range(2, b+1):
        sol(i)

    for i in range(a, b+1):
        if graph[i]:
            res += i

    print(res)