import numpy as np

FILENAME = 'input'

def load_map(filename):
	map = []
	with open(filename) as file:
		row_string = file.readline()[:-1] # Without \n
		while row_string != '':
			row_list = [int(c) for c in row_string]
			map.append(row_list)
			row_string = file.readline()[:-1]
	return np.array(map)

def initialize_visibility_map(map):
	visibility = np.full(map.shape, False)
	visibility[[0, -1], :] = True   # Edges are always visible
	visibility[:, [0, -1]] = True
	return visibility

map = load_map(FILENAME)
visibility = initialize_visibility_map(map)

for coords, height in np.ndenumerate(map[1:-1, 1:-1]): # TIL
	i = coords[0] + 1; j = coords[1] + 1
	visibility[i, j] = (
		np.all(height > map[   i,  0:j]) or
		np.all(height > map[   i, j+1:]) or
		np.all(height > map[ 0:i,    j]) or
		np.all(height > map[i+1:,    j])
	)

print('map =\n', map, '\n')
print('visibility =\n', visibility, '\n')
print(f'A total of {np.count_nonzero(visibility)} trees are visible.')
