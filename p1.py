
#This program reads a text file and prints the number of lines, words and characters in the file.
import re


word_patter = r''

characters_patter = r''

def analyze_file(file):

    with open(file) as f:
        data = f.readlines()
    num_lines = len(data)

