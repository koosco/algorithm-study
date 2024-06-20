import math

num_counter = {str(i): 0 for i in range(9)}
for num in list(input()):
    if num == '9':
        num_counter['6'] += 1
    else:
        num_counter[num] += 1
num_counter['6'] = math.ceil(num_counter['6'] / 2)
print(max(num_counter.values()))
