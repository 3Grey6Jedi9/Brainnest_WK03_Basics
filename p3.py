

def tasks02():
    j = 0
    with open('file_handling.txt') as f:
        data = f.readlines()
    for line in data:
        if j == 2:
            return f'\n{line}'
        else:
            j += 1
            continue

print(tasks02())

