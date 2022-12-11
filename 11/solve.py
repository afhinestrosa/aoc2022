from parser import Parser

FILENAME = 'input'
ROUNDS = 20

def print_monkeys(monkeys):
    for k, v in monkeys.items():
        print(v)

monkeys = Parser(FILENAME).parse_file()
print('---- INITIAL STATE ----')
print_monkeys(monkeys)

print('\n *** stuff-slinging simian shenanigans in process... ***\n')
for i in range(ROUNDS):
    for k in monkeys:
        monkeys[k].process_turn()

print('------ END STATE ------')
print_monkeys(monkeys)

item_inspected_list = [monkeys[k].items_inspected for k in monkeys]
item_inspected_list.sort()
print(f'{item_inspected_list = }')
monkey_business = item_inspected_list[-1] * item_inspected_list[-2]

print(f' *** Level of monkey business: {monkey_business}')
