f = open('input')

result_LUT = {
    'X': 0, 'Y': 3, 'Z': 6
}

play_LUT = {
    'A': {'X': 3, 'Y': 1, 'Z': 2},
    'B': {'X': 1, 'Y': 2, 'Z': 3},
    'C': {'X': 2, 'Y': 3, 'Z': 1},
}

line = f.readline()
score = 0
while line != '':
    elf_play = line[0]
    my_play = line[2]
    score += result_LUT[my_play] + play_LUT[elf_play][my_play]
    line = f.readline()

print(f'{score = }')

f.close()