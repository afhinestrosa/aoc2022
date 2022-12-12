"""
The goal was to find out the common character among the two halfs of a
string. Then, do that for all the strings (lines) in a file and convert
each character to a punctuation. The solution is the sum.

Basically, I divided each line in two parts and checked which element
was equal among them. I did that converting each part into a set and
then calling the intersection method. That gave me a character; then,
I summed up all their corresponding integers.
"""

def read_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def parse_lines(lines):
    parsed_lines = []
    for l in lines:
        parsed_lines.append(
            (l[:len(l)//2], l[len(l)//2:len(l)-1])
        )
    return parsed_lines

def char_to_points(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38
    
def compute_lines(parsed_lines):
    total = []
    for l in parsed_lines:
        I = set(l[0]).intersection(set(l[1]))
        if len(I) != 0:
            I_list = list(I)
            tmp = 0
            for i in I_list:
                tmp += char_to_points(i)
            total.append(int(tmp))
    return total

points = sum(compute_lines(parse_lines(read_lines("input.txt"))))