def search(target: int):
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if A[mid] == target:
            return True
        elif A[mid] < target:
            l = mid + 1
        elif A[mid] > target:
            r = mid - 1
    return False


n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))

for b in B:
    print(1 if search(b) else 0)
