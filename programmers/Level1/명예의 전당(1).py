from heapq import *

def solution(k, scores):
    hq, res = [], []
    for score in scores:
        if not hq:
            heappush(hq, score)
        else:
            if len(hq) == k:
                if hq[0] < score:
                    heappop(hq)
                    heappush(hq, score)
            else:
                heappush(hq, score)
        res.append(hq[0])
    return res