"""
The goal was detecting the first sequence of 14 distinct characters.

I just changed the 4s with 14s.
"""

def parse_file(filename):
    with open(filename) as f:
        a = f.readlines()
    return a[0][:len(a[0])-1]

def detect_sequence(string):
    num = 14
    for n in range(14, len(string)-14):
        sequence = list(string[n-14:n])
        if len(sequence) == len(set(sequence)):
            break
        else:
            num += 1
    return num

num = detect_sequence(parse_file("input.txt"))