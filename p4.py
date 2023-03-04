# Target and collect all the numbers put them into a list and then get the sum

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