r, c, zr, zc = map(int, input().split())
scripts = [list(input()) for _ in range(r)]
new_scripts = [[None] * c * zc for _ in range(r * zr)]

for i in range(r):
    for j in range(c):
        for k in range(zr):
            for l in range(zc):
                new_scripts[i * zr + k][j * zc + l] = scripts[i][j]

for row in new_scripts:
    print(*row, sep='')