import re
import numpy as np

def parse_file(filename):
    cargo, actions = [], []
    with open(filename) as f:
        not_ended = True
        while not_ended:
            new_line = f.readline()
            if new_line == '\n':
                not_ended = False
            else:
                cargo.append(new_line)
        not_ended = True
        while not_ended:
            new_line = f.readline()
            if new_line == '':
                not_ended = False
            else:
                actions.append(new_line)
    parsed_cargo   = transpose_cargo_matrix(
        [parse_cargo_line(l) for l in cargo[:len(cargo)-1]]
    )
    parsed_actions = [parse_action_line(l) for l in actions]
    return parsed_cargo, parsed_actions

def parse_cargo_line(line):
    parsed_line = []
    for n in range(len(line)//4):
        parsed_line.append(line[4*n+1])
    return parsed_line

def transpose_cargo_matrix(matrix):
    inv_matrix = list(np.array(matrix).T)
    parsed_matrix = []
    for n, s in enumerate(inv_matrix):
        stack_list = list(inv_matrix[n])
        not_ended = True
        while not_ended:
            try:
                stack_list.remove(' ')
            except:
                parsed_matrix.append(list(stack_list))
                not_ended = False
    return parsed_matrix

def parse_action_line(line):
    pattern = re.compile("move (?P<n1>[0-9]*) from (?P<n2>[0-9]*) to (?P<n3>[0-9]*)")
    match   = pattern.match(line[:len(line)-1])  
    return (
        int(match.group("n1")),
        int(match.group("n2")),
        int(match.group("n3"))
    )

def move_crate(parsed_cargo, num, from_crate, to_crate):
    from_stack = parsed_cargo[from_crate-1]
    to_stack   = parsed_cargo[to_crate-1]
    for n in range(num):
        elem = from_stack.pop(0)
        to_stack.insert(0,elem)
        
def move_all_crates(parsed_cargo, parsed_actions):
    for p in parsed_actions:
        move_crate(parsed_cargo, p[0], p[1], p[2])

def parse_solution(parsed_cargo):
    sol = ""
    for p in parsed_cargo:
        sol += p[0]
    return sol

pc, pa = parse_file("input.txt")
move_all_crates(pc, pa)
sol = parse_solution(pc)