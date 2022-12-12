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
    res1 = 0
    if pos != (len(tree_line) - 1):
        for t in tree_line[pos+1:]:
            if t >= tree_line[pos]:
                res1 += 1
                break
            else:
                res1 += 1
    res2 = 0
    if pos != 0:
        for t in np.flip(tree_line[:pos]):
            if t >= tree_line[pos]:
                res2 += 1
                break
            else:
                res2 += 1
    return res1 * res2

def process_forest(trees):
    X, Y = np.shape(trees)
    R = np.zeros((X,Y))
    for n in range(X):
        for m in range(Y):
            R[n,m] = (
                check_visibility(trees[n,:], m) *
                check_visibility(trees[:,m], n)
            )
    return R        

trees = parse_data(parse_file("input.txt"))
visibility = process_forest(trees)
sol = np.max(visibility)