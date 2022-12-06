from collections import deque

SIZE = 14
position = SIZE
buffer = deque([], maxlen=SIZE)

with open('input') as f:
	c = f.read(SIZE)
	[buffer.append(l) for l in c]

	while c != '' and len(set(buffer)) < SIZE:
		c = f.read(1)
		buffer.append(c)
		position += 1

print(f'{position = }')
