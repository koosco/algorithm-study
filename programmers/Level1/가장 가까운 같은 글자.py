def solution(s):
    dist = {}
    res = []
    for i, c in enumerate(s):
        if c not in dist:
            res.append(-1)
        else:
            res.append(abs(dist[c] - i))
        dist[c] = i
    return res