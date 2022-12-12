import numpy as np
import re

trans = {
    "L" : np.array([-1,  0]),
    "R" : np.array([ 1,  0]),
    "U" : np.array([ 0,  1]),
    "D" : np.array([ 0, -1])
}

def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    steps = []
    for l in lines:
        pattern = re.compile("(?P<dir>[A-Z]*) (?P<num>[0-9]*)")
        match   = pattern.match(l)
        steps.append(trans[match.group("dir")] * int(match.group("num")))
    return steps

def are_next_to_each_other(hp, tp):
    r = hp - tp
    if (np.abs(r[0]) > 0) and (np.abs(r[1]) > 0):
        return np.sum((hp - tp)**2) <= 2
    else:
        return np.sum((hp - tp)**2) <= 1

def process_tail(hp, tp):
    new_tp = np.array(tp)
    if not are_next_to_each_other(hp, tp):
        new_tp += np.sign(hp - tp)
    return new_tp

def calculate_tail_path(head_steps):
    tail_steps = []
    head_pos = np.array([0, 0])
    tail_pos = np.array([0, 0])
    tail_steps.append(tuple(tail_pos))
    for s in head_steps:
        ns = int(np.sqrt(np.sum(s**2))) # num of unit steps
        us = s // ns                     # unit step
        for n in range(ns):
            head_pos += us
            tail_pos = process_tail(head_pos, tail_pos)
            tail_steps.append(tuple(tail_pos))
    return tail_steps

steps = parse_file("input.txt")
path  = calculate_tail_path(steps)
poses = len(set(path))