import re

TOTAL_SPACE = 70000000
NEEDED      = 30000000

def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    for n, l in enumerate(lines):
        lines[n] = l[:len(l)-1]
    return lines

def generate_filesystem(lines):
    directories = {}
    path = []
    for l in lines:
        if l[0] == '$':
            if l[2:4] == 'cd':
                if l[5:] == '..':
                    path.pop(len(path)-1)
                elif l[5:] == '/':
                    path = ['/']
                else:
                    path.append(l[5:])
                if "/".join(path) not in directories:
                    directories["/".join(path)] = 0
        else:
            if l[0:3] != 'dir':
                pattern = re.compile("(?P<size>[0-9]*) (?P<name>[a-z]*)")
                match   = pattern.match(l)
                for n, _ in enumerate(path):
                    p = "/".join(path[:n+1])
                    directories[p] += int(match.group("size"))
    return directories

fs = generate_filesystem(parse_file("input.txt"))
OCCUPIED = fs['/']
TO_FREE = NEEDED - (TOTAL_SPACE - OCCUPIED)

def find_smallest_directory(fs, to_free = TO_FREE):
    fs_sorted = sorted(fs.items(), key=lambda x: x[1])
    for tup in fs_sorted:
        if tup[1] < to_free:
            continue
        else:
            return tup[1]
        
sol = find_smallest_directory(fs)