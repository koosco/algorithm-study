def solution(s):
    word_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    res, tmp = [], []
    for c in s:
        if c.isdigit():
            res.append(c)
        else:
            tmp.append(c)
        if ''.join(tmp) in word_dict:
            res.append(word_dict[''.join(tmp)])
            tmp = []
    if tmp:
        res.append(word_dict[''.join(tmp)])
    return int(''.join(res))