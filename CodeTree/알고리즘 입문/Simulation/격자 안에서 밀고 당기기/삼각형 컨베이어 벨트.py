import sys
read = sys.stdin.readline

n, t = map(int, read().split())
belt = list(map(int, read().split())) + list(map(int, read().split())) + \
            list(map(int, read().split()))

t %= (3 * n)
belt = belt[len(belt)-t:] + belt[:len(belt)-t]
print(*belt[:n])
print(*belt[n:2*n])
print(*belt[2*n:])
