mapper = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
origin_word = input()
for word in mapper:
    origin_word = origin_word.replace(word, '*')
print(len(origin_word))