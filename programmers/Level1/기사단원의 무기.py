def get_prime(number):
    ret = []
    for i in range(1, int(number ** .5) + 1):
        if not number % i:
            ret.append(number // i)
            ret.append(i)
    return len(set(ret))


def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        attack = get_prime(num)
        if attack > limit:
            answer += power
        else:
            answer += attack
    return answer