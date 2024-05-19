import sys
read = sys.stdin.readline

n = int(read())
blocks = [int(read()) for _ in range(n)]
res = []

for _ in range(2):
    res = []
    s, e = map(lambda x: x - 1, map(int, read().split()))
    for i in range(len(blocks)):
        if not s <= i <= e:
            res.append(blocks[i])
    blocks = res[:]
print(len(blocks))
for block in blocks:
    print(block)