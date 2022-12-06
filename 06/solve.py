from collections import deque

position = 4
buffer = deque([], maxlen=4)

with open('input') as f:
	c = f.read(4)
	[buffer.append(l) for l in c]

	while c != '' and len(set(buffer)) < 4:
		c = f.read(1)
		buffer.append(c)
		position += 1

print(f'{position = }')
