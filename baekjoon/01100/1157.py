from collections import Counter

most_common = Counter(input().upper()).most_common(2)
if len(most_common) == 1:
    print(most_common[0][0])
else:
    print('?' if most_common[0][1] == most_common[1][1] else most_common[0][0])