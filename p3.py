

def tasks03():
    j = 0
    with open('file_handling.txt') as f:
        data = f.readlines()
    for line in data:
        if j == 2:
            return f'\n{line}'
        else:
            j += 1
            continue

print(tasks03())

# open the binary file for reading
with open('binary.bin', 'rb') as f:
    # read the contents of the binary file
    binary_data = f.read()

# convert the binary data to a hexadecimal string
hex_string = binary_data.hex()

# open a text file for writing
with open('hex_file.txt', 'w') as f:
    # write the hexadecimal string to the text file
    f.write(hex_string)







