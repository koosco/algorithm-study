import sys

read = sys.stdin.readline

def find_pos(v, L):
    left, right = 0, len(L) - 1
    while left < right:
        mid = left + (right - left) // 2
        if L[mid] == v:
            return mid
        elif L[mid] > v:
            right = mid - 1
        elif L[mid] < v:
            left = mid + 1

L = [1, 2, 3, 4]
print(find_pos(4, L))
# for _ in range(int(read())):
#     inputs = list(map(int, read().split()))