from sys import stdin, stdout

def get_formula():
    return stdin.readline()

def get_formulas():
    return stdin.readlines()

def send(out):
    stdout.write(str(out))
