# Author: John Landeholt [TA]
from sys import stdin, stdout

def get_formula():
    return stdin.readline().strip()

def get_formulas():
    for line in stdin:
        yield line.strip()

def send(out):
    stdout.write(str(out) + '\n')
