def solution(sizes):
    r1, r2 = [], []
    for x, y in sizes:
        if x > y:
            r1.append(x)
            r2.append(y)
        else:
            r1.append(y)
            r2.append(x)
    return max(r1) * max(r2)