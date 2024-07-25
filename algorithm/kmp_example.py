def kmp_table(pattern):
    table = [0] * len(pattern)
    head = 0
    for tail in range(1, len(pattern)):
        if head > 0 and pattern[head] != pattern[tail]:
            head = 0
        if pattern[head] == pattern[tail]:
            head += 1
            table[tail] = head
    return table


def kmp(word, pattern):
    table = kmp_table(pattern)
    results = []
    head = 0

    for tail in range(1, len(word)):
        if head > 0 and word[head] != pattern[tail]:
            head = 0
        if word[tail] == pattern[head]:
            if head == len(pattern) - 1:
                results.append(tail - len(pattern) + 1)
                head = table[head]
            else:
                head += 1
    return results
