FILENAME = 'example_2'
ROPE_LENGTH = 10

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
    elif delta_x < 0:
        movements.append('L')
    if delta_y > 0:
        movements.append('U')
    elif delta_y < 0:
        movements.append('D')

    return movements

visited_points = {(0,0)}
rope = [[0,0] for i in range(ROPE_LENGTH)]
# head = [0, 0]
# tail = [0, 0]

with open(FILENAME) as file:
    line = file.readline()
    while line != '':
        head_movement = line.split() # 0: direction; 1: no. steps
        for i in range(int(head_movement[1])):
            move(rope[0], head_movement[0])
            for j in range(1, ROPE_LENGTH):
                if not are_touching(rope[j-1], rope[j]):
                    for tail_direction in decide_tail_movements(rope[j-1], rope[j]):
                        move(rope[j], tail_direction)
                    if j == ROPE_LENGTH - 1:
                        visited_points.add(tuple(rope[j]))

        line = file.readline()

print('\n === End of simulation: ===\n')
print(f'{rope = }')
# print(visited_points)
print(f'Tail visited {len(visited_points)} positions.')
