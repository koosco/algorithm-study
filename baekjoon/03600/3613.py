variable = input()

camel, under_bar = False, False
res = []

for s in variable:
    if 'A' <= s <= 'Z':
        camel = True
    if s == '_':
        under_bar = True
if camel and under_bar:
    print('Error!')
elif camel:
    for s in variable:
        if 'A' <= s <= 'Z':
            res.append('_')
            res.append(s.lower())
        else:
            res.append(s)
elif under_bar:
    idx = 0
    while idx < len(variable):
        if variable[idx] == '_':
            idx += 1
            res.append(variable[idx].upper())
        else:
            res.append(variable[idx])
        idx += 1
print(''.join(res))

