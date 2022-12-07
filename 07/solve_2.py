AVAILABLE = 70000000
NEEDED = 30000000
SIZE_MAX = 100000

class Node:
	solution_2 = AVAILABLE
	solution = 0

	def __init__(self, name, type, size, parent=None):
		self.name = name
		self.type = type
		self.size = size
		self.children = []
		self.parent = parent

	def add_child(self, node):
		self.children.append(node)
		node.parent = self

	def __str__(self):
		if self.type == 'file':
			text = f'{self.name} ({self.type}, size={self.size})\n'
		else:
			extra_text = f', size={self.size}' if self.size > 0 else ''
			text = f'{self.name} (dir{extra_text})\n'
			for child in self.children:
				text += str(child)
		return text

	def calculate_size(self):
		if self.type == 'dir':
			size = 0
			for child in self.children:
				size += child.calculate_size()
			if size <= SIZE_MAX:
				Node.solution += size
			self.size = size
		return self.size

	def find_delete_candidate(self, needed_size):
		if self.type == 'dir':
			for child in self.children:
				child.find_delete_candidate(needed_size)
			if self.size < Node.solution_2 and self.size >= needed_size:
				Node.solution_2 = self.size


class Tree(Node):
	def __init__(self):
		super().__init__('/', 'dir', 0)



status = 'WAIT_CMD'
root = Tree()
current_dir = root

with open('input') as file:
	line = file.readline() # skip cd /

	line = file.readline().split()
	while len(line) > 0:
		print(f'Processing: {line}')
		if status == 'WAIT_CMD':  # line[0]: $; line[1]: cmd; line[2]: arg;
			if line[1] == 'ls':
				status = 'LIST_DIR'
			elif line[1] == 'cd':
				if line[2] == '..':
					current_dir = current_dir.parent
				else:
					current_dir = next(x for x in current_dir.children if x.name == line[2])
		elif status == 'LIST_DIR':
			if line[0] == '$':
				status = 'WAIT_CMD'
				continue
			elif line[0] == 'dir':
				current_dir.add_child(Node(
					name=line[1],
					type='dir',
					size=-1,
				))
			else:
				current_dir.add_child(Node(
					name=line[1],
					type='file',
					size=int(line[0]),
				))

		line = file.readline().split()

root.calculate_size()
print(root)
root.find_delete_candidate(root.size - (AVAILABLE - NEEDED))
print(f'{Node.solution = }')
print(f'{Node.solution_2 = }')
