import parse_to_string as Stringer
import filter_string as Filter
import matching_engine as Matcher
import sys
import argparse

#make sure cli gets the right number of arguements
if len(sys.argv) < 2:
    print("Usage: python pipeline.py <file1> <file2>")
    sys.exit(1)

#fetch both files given as CLI arguements
parser = argparse.ArgumentParser(description='Provide jobs')
parser.add_argument('files', nargs='+', help='input files')

args = parser.parse_args()

file1, file2 = args.files[:2]

#the following would use the Stringer if using pure pdf but for 
#now using txt files

file1 = open(file1).read()
file2 = open(file2).read()

# Filter both strings and output lists

file1 = Filter.filter_string(file1)
file2 = Filter.filter_string(file2)

#match both files and output a result

Matcher.matchingEngine(file1,file2)


