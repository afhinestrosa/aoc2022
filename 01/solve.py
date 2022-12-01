# Challenge: find the maximum calories carried by an elf

f = open('input')

text = f.readline()
maximum_calories = 0
current_maximum_calories = 0
while text != '':
    if text != '\n':
        current_maximum_calories += int(text)
    else:
        if current_maximum_calories > maximum_calories:
            maximum_calories = current_maximum_calories
        current_maximum_calories = 0
    text = f.readline()

f.close()
print(maximum_calories)

