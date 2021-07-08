#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import argparse
import re

#Add argument options
parser = argparse.ArgumentParser(description="program that prints matching strings for files in a given directory")
parser.add_argument('-d', '--dir', help="directory to run (default is CWD)")
args = parser.parse_args()

if args.dir:
    directory = args.dir
else:
    directory = './'

onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

#find strings using python and return the results specified
def findstrings(encoding, file, min=4):
    results = {}
    with open(f'{directory}{file}', 'rb') as f:
        f.data = f.read()
        results['ascii'] = [s.decode('utf-8', 'ignore') for s in re.findall(b'[\x1f-\x7e]{%d,}' % min, f.data)]
        results['wide'] = [s.decode('utf-16le', 'ignore') for s in re.findall(b'(?:[\x1f-\x7e][\x00]){%d,}' % min, f.data)]
    return results[encoding]

def print_formatted(string_result, encoding):
    for i,x in enumerate(string_result):
        print(f'$string{encoding[0]}{i} = \"{x}\" {encoding}')

def print_banner(header):
    print("-" * 25, header, "-" * 25)

#do a bitwise AND for any amount of strings in the files we're working with and print it in a yara friendly format 
def find_matches(encoding):
    string_result = set(findstrings(encoding, onlyfiles[0]))
    for f in onlyfiles[1:]:
        string_result &= set(findstrings(encoding, f))
    print_formatted(string_result, encoding)

if __name__ == "__main__":
    print_banner("ASCII")
    find_matches("ascii")
    print_banner("WIDE LE")
    find_matches("wide")