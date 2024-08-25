def solution(begin, target, words):
    def count_diff(w1, w2):
        ret = 0
        for i in range(n):
            if w1[i] != w2[i]:
                ret += 1
                if ret > 1:
                    return False
        return ret == 1

    def sol(current_word: str, depth: int = 0):
        nonlocal res
        if current_word == target:
            res = min(res, depth)
            return
        if depth > res:
            return
        for word in words:
            if word not in visited and count_diff(current_word, word):
                visited.add(word)
                sol(word, depth + 1)
                visited.discard(word)

    n = len(begin)
    res = 51
    visited = {begin}
    sol(begin)
    return res if res != 51 else 0
