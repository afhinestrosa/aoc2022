f = open('input')

result_LUT = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}

play_LUT = {'X' : 1, 'Y' : 2, 'Z' : 3}

line = f.readline()
score = 0
while line != '':
    elf_play = line[0]
    my_play = line[2]
    score += result_LUT[elf_play][my_play] + play_LUT[my_play]
    line = f.readline()

print(f'{score = }')

f.close()