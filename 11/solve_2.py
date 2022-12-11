from parser import Parser

FILENAME = 'input'
ROUNDS = 10_000

def print_monkeys(monkeys):
    for k, v in monkeys.items():
        print(v)

inspections = []
monkeys = Parser(FILENAME).parse_file(relief_operation=False)
for i in range(ROUNDS):
    for k in monkeys:
        monkeys[k].process_turn()
    if (i+1) % 1000 == 0:
        print(f'Round {i+1}')
        item_inspected_list = [monkeys[k].items_inspected for k in monkeys]
        print(item_inspected_list)

item_inspected_list = [monkeys[k].items_inspected for k in monkeys]

print(f'{item_inspected_list = }')
item_inspected_list.sort()
monkey_business = item_inspected_list[-1] * item_inspected_list[-2]
print(f'{monkey_business = }')
