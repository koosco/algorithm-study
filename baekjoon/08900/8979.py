import sys

read = sys.stdin.readline

n, k = map(int, read().split())
countries = [list(map(int, read().split())) for _ in range(n)]
grade = [1] * 1001
for country1 in countries:
    for country2 in countries:
        if country1[0] == country2[0]:
            continue
        country_id = country1[0]
        if country1[1] < country2[1]:
            grade[country_id] += 1
        elif country1[1] == country2[1] and country1[2] < country2[2]:
            grade[country_id] += 1
        elif country1[1] == country2[1] and country1[2] == country2[2] and \
                country1[3] < country2[3]:
            grade[country_id] += 1
print(grade[k])