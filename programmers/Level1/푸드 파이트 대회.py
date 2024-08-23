def solution(food):
    s = ''
    for i, f in enumerate(food[1:]):
        f //= 2
        s += str(i+1) * f
    return s + '0' + s[::-1]