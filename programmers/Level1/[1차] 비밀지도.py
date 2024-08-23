def solution(n, arr1, arr2):
    res = []
    arr1 = list(map(lambda x: list(map(int, list(bin(x)[2:].zfill(n)))), arr1))
    arr2 = list(map(lambda x: list(map(int, list(bin(x)[2:].zfill(n)))), arr2))
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append('#' if arr1[i][j] or arr2[i][j] else ' ')
        res.append(''.join(tmp))
    return res
