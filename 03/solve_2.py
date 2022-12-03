def get_item(priority):
	if 1 <= priority <= 26:
		item = chr(priority + ord('a') - 1)
	elif 27 <= priority <= 52:
		item = chr(priority - 27 + ord('A'))
	else:
		item = None
	return item

def read_group(file):
	return [file.readline() for i in range(3)]

file = open('input')

sum_priorities = 0

group = read_group(file)
while group[0] != '':
	for p in range(1, 53):
		item = get_item(p)
		if item in group[0] and item in group[1] and item in group[2]:
		   sum_priorities += p
	group = read_group(file)

print(f'{sum_priorities = }')

file.close()
