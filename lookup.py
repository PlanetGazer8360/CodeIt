import re
from argparse import *

def main():
    parser= ArgumentParser()
    parser.add_argument('-w', '--word', help= 'Specify a word you want to search for')
    parser.add_argument('-fn','--FileName', help= 'Specify the file you want to search the word in')
    args= parser.parse_args()

    searchFile = open(args.fn)
    lineNum= 0

    for line in searchFile.readlines():
        line = line.strip('\n\r')
        lineNum += 1
        searchResult = re.search(args.word,line, re.M|re.I)
        if searchResult:
            print(str(lineNum)+ ': ' + line)

if __name__ == '__main__':
    main()