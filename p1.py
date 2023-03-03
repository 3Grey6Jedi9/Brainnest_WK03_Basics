
#This program reads a text file and prints the number of lines, words and characters in the file.
import re

file = 'file_handling.txt'

word_patter = r'[A-Za-z]+'

characters_patter = r'\S'


def analyze_file(file):
    words = []
    num_words = []
    characters = []
    num_char = []
    with open(file) as f:
        data = f.readlines()
    num_lines = len(data)
    for line in data:
        matchw = re.findall(word_patter, line)
        matchchar = re.findall(characters_patter, line)
        words.append(matchw)
        characters.append(matchchar)
    for line in words:
        num_words.append(len(line))
    for line in characters:
        num_char.append(len(line))
    return f'''The number lines in the file is {num_lines}, the number of words in the file is {sum(num_words)}
and the number of characters in the file is (whitespaces are not considered) {sum(num_char)}'''

print(analyze_file(file))



