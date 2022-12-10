FILENAME = 'example'
status = 'NOOP'
cycle = 1
X = 1
add = 0
total_signal_strength = 0

with open(FILENAME) as file:
    line = file.readline().split()
    while len(line) > 0:
        if (cycle == 20) or (cycle - 20) % 40 == 0:
            total_signal_strength += cycle * X
        if status != 'ADD':
            if line[0] == 'noop':
                line = file.readline().split()
            elif line[0] == 'addx':
                add = int(line[1])
                status = 'ADD'
        else:
            X += add
            status = 'NOOP'
            line = file.readline().split()
        cycle += 1
        print(f'{cycle = }')
        print(f'{line = }')

print(f'{total_signal_strength = }')
