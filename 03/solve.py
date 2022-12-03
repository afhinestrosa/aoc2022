def get_priority(item):
    item_lowercase = item.lower()
    priority = ord(item_lowercase) - ord('a') + 1
    if ord('A') <= ord(item) <= ord('Z'):
        priority += 26
    return priority

file = open('input')

sum_priorities = 0

line = file.readline()
while line != '':
	compartment_1 = line[0:len(line)//2]
	compartment_2 = line[len(line)//2:]
	for item in compartment_1:
		if item in compartment_2:
			sum_priorities += get_priority(item)
			break
	line = file.readline()

print(f'{sum_priorities = }')

file.close()
