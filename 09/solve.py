FILENAME = 'input'

def are_touching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def move(point, direction):
    if direction == 'R':
        point[0] += 1
    elif direction == 'L':
        point[0] -= 1
    elif direction == 'U':
        point[1] += 1
    elif direction == 'D':
        point[1] -= 1

def decide_tail_movements(head, tail):
    movements = []
    delta_x = head[0] - tail[0]
    delta_y = head[1] - tail[1]

    if delta_x > 0:
        movements.append('R')
    if delta_x < 0:
        movements.append('L')
    if delta_y > 0:
        movements.append('U')
    if delta_y < 0:
        movements.append('D')

    return movements

visited_points = set()
head = [0, 0]
tail = [0, 0]

with open(FILENAME) as file:
    line = file.readline()
    while line != '':
        head_movement = line.split() # 0: direction; 1: no. steps
        for i in range(int(head_movement[1])):
            move(head, head_movement[0])
            if not are_touching(head, tail):
                for tail_direction in decide_tail_movements(head, tail):
                    move(tail, tail_direction)
                    visited_points.add(tuple(tail))

        line = file.readline()

print(f'{head = }, {tail = }')
print(f'Tail visited {len(visited_points)} positions.')
