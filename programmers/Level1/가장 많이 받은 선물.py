from typing import List, Dict
from collections import defaultdict


def solution(friends: List[str], gifts: List[str]):
    n: int = len(friends)
    friend_idx_dict: Dict[str, int] = defaultdict(int)
    table: List[List[int]] = [[0] * n for _ in range(n)]
    gift_idx: List[int] = [0] * n
    ret: List[int] = [0] * n

    for i, name in enumerate(friends):
        friend_idx_dict[name] = i

    for gift in gifts:
        x, y = gift.split()
        i_x, i_y = friend_idx_dict[x], friend_idx_dict[y]
        table[i_x][i_y] += 1
        gift_idx[i_x] += 1
        gift_idx[i_y] -= 1

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if table[i][j] > table[j][i]:
                ret[i] += 1
            elif table[i][j] == table[j][i] and gift_idx[i] > gift_idx[j]:
                ret[i] += 1
    return max(ret)
