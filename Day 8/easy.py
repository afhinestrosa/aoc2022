import numpy as np

def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    for n, l in enumerate(lines):
        lines[n] = l[:len(l)-1]
    return lines

def parse_data(lines):
    parsed_lines = []
    for l in lines:
        numbers = list(l)
        for i, num in enumerate(numbers):
            numbers[i] = int(num)
        parsed_lines.append(np.array(numbers))
    return np.array(parsed_lines)

def check_visibility(tree_line, pos):
    val = True
    if (pos != 0) and (pos != (len(tree_line) - 1)):
        res1 = True
        for t in tree_line[pos+1:]:
            if t >= tree_line[pos]:
                res1 = False
        res2 = True
        for t in tree_line[:pos]:
            if t >= tree_line[pos]:
                res2 = False
        val = res1 or res2
    return val

def process_forest(trees):
    X, Y = np.shape(trees)
    R = np.zeros((X,Y), dtype = bool)
    for n in range(X):
        for m in range(Y):
            R[n,m] = (
                check_visibility(trees[n,:], m) or
                check_visibility(trees[:,m], n)
            )
    return R        

trees = parse_data(parse_file("input.txt"))
visibility = process_forest(trees)
total = np.sum(visibility)