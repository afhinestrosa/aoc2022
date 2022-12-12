"""
Insted of finding the maximum, find the top three maxima.

I sorted the list and then took the three last elements.
"""
def parse(list_of_lines):
    list_of_lists_of_nums = []
    tmp_list = []
    for pos, line in enumerate(list_of_lines):
        if line != '\n':
            tmp_list.append(int(line))
        else:
            list_of_lists_of_nums.append(list(tmp_list))
            tmp_list = []
    list_of_lists_of_nums.append(list(tmp_list))
    return list_of_lists_of_nums

def add(calories_lists):
    a = []
    for c in calories_lists:
        a.append(sum(c))
    return a

with open("input.txt") as f:
    list_of_lines = f.readlines()
    
CaloriesList = parse(list_of_lines)
elf = max(add(CaloriesList))

Elfs = add(CaloriesList)
Elfs.sort()
total = sum(Elfs[-1:-4:-1])