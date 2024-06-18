import sys

read = sys.stdin.readline


def checker(word: str):
    visited = set()
    prev = word[0]
    visited.add(word[0])
    for letter in word[1:]:
        if prev == letter:
            continue
        else:
            if letter not in visited:
                visited.add(letter)
                prev = letter
            else:
                return False
    return True



res = 0
for _ in range(int(read())):
    if checker(read().rstrip()):
        res += 1
print(res)