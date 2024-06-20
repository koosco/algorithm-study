import sys

read = sys.stdin.readline

subject_grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

subjects = [read().split() for _ in range(20)]
total_credit, max_credit = 0, 0
for _, credit, score in subjects:
    if score == 'P':
        continue
    total_credit += float(credit) * subject_grade[score]
    max_credit += float(credit)
print(round(total_credit / max_credit, 6))
