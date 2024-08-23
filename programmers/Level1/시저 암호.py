def solution(s, n):
    L = [chr(97 + i) for i in range(26)]
    U = [chr(65 + i) for i in range(26)]
    res = []

    for c in s:
        if c in L:
            res.append(L[(ord(c) - 97 + (n % 26)) % 26])
        elif c in U:
            res.append(U[(ord(c) - 65 + (n % 26)) % 26])
        elif c == ' ':
            res.append(c)
    return ''.join(res)