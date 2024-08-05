def sol(path: str, idx: int = 1, depth: int = 0):
    if depth == k:
        if eval(path):
            res.append(''.join(path[::2]).zfill(k + 1))
        return
    if path != '0' and not eval(path):
        return
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            sol(path + ops[idx] + str(i), idx + 1, depth + 1)
            visited[i] = False


k = int(input())
ops = [''] + input().split()
visited = [False] * 10
res = []
for i in range(10):
    visited[i] = True
    sol(str(i))
    visited[i] = False
print(res[-1], res[0], sep='\n')
