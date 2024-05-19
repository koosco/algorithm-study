n = int(input())

cnt = 0
for i in range(n):
    for j in range(n):
        print(cnt % 9 + 1, end=' ')
        cnt += 1
    print()