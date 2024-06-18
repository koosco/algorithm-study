import sys

read = sys.stdin.readline

n = int(read())
people = [list(map(int, read().split())) + [1] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            people[i][2] += 1
print(*[x[2] for x in people])
