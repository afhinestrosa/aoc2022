def get_ranges(line):
	elves = line.split(',')
	elves = [e.split('-') for e in elves]
	elves_ranges = [range(int(e[0]), int(e[1]) + 1) for e in elves]
	return elves_ranges

def is_there_overlap(ranges):
	ranges_01 = [k in ranges[1] for k in ranges[0]]
	ranges_10 = [k in ranges[0] for k in ranges[1]]
	return all(ranges_01) or all(ranges_10)

num_overlaps = 0
with open('input') as file:
	line = file.readline()
	while line != '':
		ranges = get_ranges(line)
		num_overlaps += is_there_overlap(ranges)
		line = file.readline()
print(f'{num_overlaps = }')
