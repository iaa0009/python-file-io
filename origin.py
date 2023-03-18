#!/usr/bin/env python

import re
import sys

def find_word(file, pattern):
    """
    This function is to parse a given file to find a certain pattern/word and then writes the output into a new file.
    
    Returns
    -------
    A file that contains a list of all matches of the pattern in the original file with the line number it was found on and the word itself separated by a tab.
    
    """
# using a reg expression to match the initial and the last letters and ignore the letter case 
#    pattern = re.compile(r'\b(herita\w*|inherit\w*)\b', re.IGNORECASE)
#to make the script more flexible 
    pattern = re.compile(pattern, re.IGNORECASE)
# naming the output file after the input one
    output = file + '_output'
# open the original file to read and in parallel open a new file to write the output to
    with open(file, 'r') as f:
        with open(output, 'w') as wf:
# iterate over each line in the file and counts
            for i, line in enumerate(f):
# find all matches of the pattern in the line
                for match in re.findall(pattern, line):
# write each match to the output file separated by a tab from the count
                    wf.write(f"{i+1}\t{match}\n")

def main():

#The user should provide the script name, inputfile name, as well as a pattern, otherwise the script will give an error then exit
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file pattern")
        sys.exit(1)
#the 2nd argument is the inputfile name and the 3rd is the pattern
    file = sys.argv[1]
    pattern = sys.argv[2]
# call the function with the provided inputfile name and pattern
    find_word(file, pattern)

if __name__ == '__main__':
    main()

