"""
So, this was just some paper-scissors-rock games. A, B and C are meant to
be rock, paper and scissors, respectively; same for X, Y and Z. The first
three are the symbols used for the enemy and the second three are the ones
used for yourself. Each game is represented by a pair of symbols (e.g. AX)
and the goal is to find the puntuation for each game based on some stats.

There are tons of games in a file, so I read them, translated into a pair
of characters and made two dictionaries as LUT containing the points for
each character combination. Then, I summed up all the points to get the
answer.
"""

selection_score = {
    'X' : 1, # you choose rock
    'Y' : 2, # you choose paper
    'Z' : 3  # you choose scissors
}

outcome_score = {
    'X' : { # you choose rock
        'A' : 3, # they choose rock
        'B' : 0, # they choose paper
        'C' : 6, # they choose scissors
    },
    'Y' : { # you choose paper
        'A' : 6, # they choose rock
        'B' : 3, # they choose paper
        'C' : 0, # they choose scissors
    },
    'Z' : { # you choose scissors
        'A' : 0, # they choose rock
        'B' : 6, # they choose paper
        'C' : 3, # they choose scissors
    },
}

def calculate_score(*args):
    scores = []
    for a in args:
        scores.append(selection_score[a[1]] + outcome_score[a[1]][a[0]])
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