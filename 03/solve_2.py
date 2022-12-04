def get_priority(item):
    item_lowercase = item.lower()
    priority = ord(item_lowercase) - ord('a') + 1
    if ord('A') <= ord(item) <= ord('Z'):
        priority += 26
    return priority

def read_group(file):
	return [file.readline()[:-1] for i in range(3)] # :-1 excludes \n

file = open('input')

sum_priorities = 0

group = read_group(file)
while group[0] != '':
	for item in set(group[0]):
		if item in group[1] and item in group[2]:
		   sum_priorities += get_priority(item)
	group = read_group(file)

print(f'{sum_priorities = }')

file.close()
