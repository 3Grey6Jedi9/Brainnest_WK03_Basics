#target blank rows and remove them modifying the original file



import re

pattern_blank = r'^[\s]+$'

with open('testp5.txt') as f:
    lines = f.readlines()

non_blank_lines = []

for line in lines:
    if not re.match(pattern_blank, line):
        non_blank_lines.append(line)

with open('testp5.txt', 'w') as f:
    f.writelines(non_blank_lines)
