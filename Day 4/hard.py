import re
import numpy as np

def parse_line(string):
    pattern = re.compile("(?P<n1>[0-9]*)-(?P<n2>[0-9]*),(?P<n3>[0-9]*)-(?P<n4>[0-9]*)")
    match   = pattern.match(string)
    
    return (
        (int(match.group("n1")), int(match.group("n2"))),
        (int(match.group("n3")), int(match.group("n4"))),
    )

def parse_file(filename):
    parsed_lines = []
    with open(filename) as f:
        lines = f.readlines()
    for l in lines:
        parsed_lines.append(parse_line(l))
    return parsed_lines

def compute_lines(parsed_lines):
    results = []
    for p in parsed_lines:
        a = set(list(np.arange(p[0][0], p[0][1] + 1E-3, dtype = int)))
        b = set(list(np.arange(p[1][0], p[1][1] + 1E-3, dtype = int)))
        if a.intersection(b) == set():
            results.append(0)
        else:
            results.append(1)
    return results

total = sum(compute_lines(parse_file("input.txt")))