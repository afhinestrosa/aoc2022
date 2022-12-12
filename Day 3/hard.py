"""
Similar to the easy part: the goal is to find out the common character
among each group of three lines of a file.

I just modified the 'parse_lines' function to store them as a list of
tuples with three strings, and then the 'compute_lines' function to 
make the intersection of each set of characters of each tuple.
"""

def read_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def parse_lines(lines):
    parsed_lines = []
    for n in range(len(lines)//3):
        parsed_lines.append(
            (
                lines[3*n][:len(lines[3*n])-1],
                lines[3*n+1][:len(lines[3*n+1])-1],
                lines[3*n+2][:len(lines[3*n+2])-1],
            )
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
        I = set(l[0]).intersection(set(l[1])).intersection(set(l[2]))
        if len(I) != 0:
            I_list = list(I)
            tmp = 0
            for i in I_list:
                tmp += char_to_points(i)
            total.append(int(tmp))
    return total

result = sum(compute_lines(parse_lines(read_lines("input.txt"))))