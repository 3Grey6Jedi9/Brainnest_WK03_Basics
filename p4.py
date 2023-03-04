# Target and collect all the numbers put them into a list and then get the sum

import re


def tasks04():
    j = 0
    with open('file_handling.txt') as f:
        data = f.readlines()
    for line in data:
        if j == 3:
            return f'\n{line}'
        else:
            j += 1
            continue

print(tasks04())



pattern_numbers = r'\d'

with open('testp4.txt') as f:
    data = f.read()
    text_numbers = re.findall(pattern_numbers, data)
    int_numbers = [int(n) for n in text_numbers]




print(sum(int_numbers))