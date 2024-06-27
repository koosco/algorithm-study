from typing import List
from itertools import groupby


def get_longest_length(L: List[int]):
    return max([len(list(g)) for _, g in groupby(L)], default=0)


print(get_longest_length([1, 1, 1, 2, 3, 4]))
