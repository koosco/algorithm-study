def solution(name, yearning, photo):
    scores = {n: y for n, y in zip(name, yearning)}
    res = []
    for p in photo:
        tmp = 0
        for e in p:
            if e in scores:
                tmp += scores[e]
        res.append(tmp)
    return res