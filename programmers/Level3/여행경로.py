from typing import List, Set


def solution(tickets):
    res = None
    visited = [False] * len(tickets)
    tickets.sort(key=lambda x: x[1])
    def sol(path=['ICN']):
        if len(path) == len(tickets) + 1:
            nonlocal res
            res = path[:]
            return True
        for i, ticket in enumerate(tickets):
            s, e = ticket
            if not visited[i] and path[-1] == s:
                visited[i] = True
                ret = sol(path+[e])
                visited[i] = False
                if ret:
                    return True
    sol()
    return res