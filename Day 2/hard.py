"""
Same thing as the easy part, but now the X, Y and Z represents that you
should look for losing, getting a draw or winning, respectively.

The solution is as easy as changing the dictionaries and how the points
are given, but the skeleton of the code is the same one.
"""

translation = {
    'A' : { # they choose rock
        'X' : 3,
        'Y' : 1,
        'Z' : 2,
    },
    'B' : { # they choose paper
        'X' : 1,
        'Y' : 2,
        'Z' : 3,
    },
    'C' : { # they choose scissors
        'X' : 2,
        'Y' : 3,
        'Z' : 1,
    },
}

outcome_score = {
    'X' : 0, # you need to lose
    'Y' : 3, # you need to draw
    'Z' : 6  # you need to win
}

def calculate_score(*args):
    scores = []
    for a in args:
        scores.append(outcome_score[a[1]] + translation[a[0]][a[1]])
    return sum(scores)

def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    results = []
    for l in lines:
        results.append((l[0], l[-2]))
    return results

res   = parse_file("input.txt")
score = calculate_score(*res)