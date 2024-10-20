def get_tree(h: int) -> bool:
    ret: int = 0
    for tree in trees:
        ret += max(0, tree - h)
        if ret >= m:
            return True
    return False


n, m = map(int, input().split())
trees = list(map(int, input().split()))
l, r = 0, max(trees)
while l <= r:
    mid: int = l + (r - l) // 2
    if get_tree(mid):
        l = mid + 1
    else:
        r = mid - 1
print(r)