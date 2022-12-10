FILENAME = 'example'
status = 'NOOP'
cycle = 1
X = 1
add = 0
total_signal_strength = 0

def draw_sprite(position):
    sprite = ''
    for i in range(40):
        if position-1 <= i <= position+1:
            sprite += '#'
        else:
            sprite += '.'
    return sprite

sprite = draw_sprite(X)

with open(FILENAME) as file:
    line = file.readline().split()
    while len(line) > 0:
        # Render CRT
        print(sprite[(cycle-1) % 40], end='')
        if cycle % 40 == 0: print()

        # Part 1 logic
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
            sprite = draw_sprite(X)

        cycle += 1

print(f'\n{total_signal_strength = }')
