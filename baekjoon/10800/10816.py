import sys

read = sys.stdin.readline

read().rstrip()
cards = list(map(int, read().split()))
cards_dict = {}
read().rstrip()
nums = list(map(int, read().split()))

for card in cards:
    if card not in cards_dict:
        cards_dict[card] = 0
    cards_dict[card] += 1

for num in nums:
    print(cards_dict[num] if num in cards_dict else 0, end=' ')
