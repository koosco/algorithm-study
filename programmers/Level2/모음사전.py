from typing import List


def solution(word):
    def sol(path: str, depth: int, idx: List[int]):
        if depth > 5:
            return
        idx[0] += 1
        if path == word:
            nonlocal res
            res = idx[0]
            return True
        for s in list('AEIOU'):
            if sol(path + s, depth + 1, idx):
                return True

    res = 0
    sol('', 0, [-1])

    return res