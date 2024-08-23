def solution(a, b, n):
    res = 0

    while n >= a:
        rest = n % a
        n = n // a * b
        res += n
        n += rest
    return res