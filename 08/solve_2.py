import numpy as np

FILENAME = 'input'

def load_map(filename):
	map = []
	with open(filename) as file:
		row_string = file.readline()[:-1] # Without \n
		while row_string != '':
			row_list = [int(c) for c in row_string]
			map.append(row_list)
			row_string = file.readline()[:-1] # Without \n
	return np.array(map)

def initialize_score_map(map):
	score = np.zeros(map.shape, dtype=int)
	return score

def scan_view(height, view):
	score = 0
	for tree in view:
		score += 1
		if tree >= height:
			break
	return score

map = load_map(FILENAME)
score = initialize_score_map(map)

for coords, height in np.ndenumerate(map[1:-1, 1:-1]):
	i = coords[0] + 1; j = coords[1] + 1
	score[i, j] = (
		scan_view(height, np.flip(np.ravel(map[   i,  0:j]))) *
		scan_view(height, 		  np.ravel(map[   i, j+1:]))  *
		scan_view(height, np.flip(np.ravel(map[ 0:i,    j]))) *
		scan_view(height, 		  np.ravel(map[i+1:,    j]))
	)

print('map =\n',  map, '\n')
print('score =\n', score, '\n')
print(f'The highest score is {np.max(score)}.')
