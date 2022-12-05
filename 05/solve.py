import re
from collections import deque

with open('input') as f:
    # Read initial state
    line = f.readline()
    scenario = []
    while line[0:3] != ' 1 ':
        scenario.append(line[:-1])
        line = f.readline()
    num_stacks = int(line[-2])

    # Initialize deques
    stacks = [deque() for i in range(num_stacks)]
    for line in scenario:
        for i_stack in range(num_stacks):
            position = 1 + i_stack*4
            if position < len(line):
                letter = line[1 + i_stack*4]
                if letter != ' ': stacks[i_stack].append(letter)
            else:
                break

    f.readline() # Skips whiteline

    # Read and execute moves
    line = f.readline()
    while line != '':
        play = [int(s) for s in re.findall(r'\d+', line)]
        p_move = play[0];   p_from = play[1];   p_to = play[2]
        [stacks[p_to-1].appendleft(stacks[p_from-1].popleft()) for i in range(p_move)]
        line = f.readline()

# Format answer for submitting
answer = ''
for stk in stacks:
    answer += stk[0]
print(f'{answer = }')