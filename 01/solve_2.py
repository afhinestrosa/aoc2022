# Challenge: find the maximum calories carried by an elf (top 3)

top_3 = [0, 0, 0]

def insert_in_top(top, element):
    for k in range(len(top)):
        if element > top_3[k]:
            for kk in reversed(range(k, len(top)-1)):
                top[kk+1] = top[kk]
            top[k] = element
            break

f = open('input')
text = f.readline()
maximum_calories = 0
current_maximum_calories = 0
while text != '':
    if text != '\n':
        current_maximum_calories += int(text)
    else:
        insert_in_top(top_3, current_maximum_calories)
        current_maximum_calories = 0
    text = f.readline()

print(sum(top_3))

f.close()
