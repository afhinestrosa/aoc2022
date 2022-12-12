"""
The goal was detecting the first sequence of 4 distinct characters.

The file was just a line, so I converted it to a string and then I
processed each group of four characters. I had to be careful with the
answer, because if the match sequence was to be in the first four characters
that's a 4 answer (4 characters have arrived).
"""

def parse_file(filename):
    with open(filename) as f:
        a = f.readlines()
    return a[0][:len(a[0])-1]

def detect_sequence(string):
    num = 4
    for n in range(4, len(string)-4):
        sequence = list(string[n-4:n])
        if len(sequence) == len(set(sequence)):
            break
        else:
            num += 1
    return num

num = detect_sequence(parse_file("input.txt"))