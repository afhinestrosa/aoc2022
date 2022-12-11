from monkey import Monkey

class Parser:
    def __init__(self, filename):
        self.filename = filename

    def parse_file(self, relief_operation=True):
        monkeys = {}
        with open(self.filename) as file:
            monkey = self.parse_monkey(file, relief_operation)
            while monkey is not None:
                monkeys[monkey.id] = monkey
                monkey = self.parse_monkey(file, relief_operation)
        limit = 1
        for k in monkeys:
            limit *= monkeys[k].test_divisible
        for k in monkeys:
            monkeys[k].limit = limit
        Monkey.other_monkeys = monkeys
        return monkeys

    def parse_monkey(self, file, relief_operation):
        line = file.readline()
        lines = []
        monkey = None
        while line not in ('\n', ''):
            lines.append(line)
            line = file.readline()
        if lines:
            # First line is ID
            monkey_no = int(lines[0][7:-2])
            # Second line is Starting items:
            items_str = lines[1][17:-1].split(',')
            items = [int(item) for item in items_str]
            # Third line is Operation: new =
            operation_str = lines[2][19:-1]
            # Fourth line is Test: divisible by N
            test_divisible = int(lines[3][20:-1])
            # Fifth line is "    If true: throw to monkey N"
            throw_true = int(lines[4][29:-1])
            # Sixth line is "    If false: throw to monkey N"
            throw_false = int(lines[5][30:-1])
            monkey = Monkey(
                id=monkey_no,
                starting_items=items,
                operation=operation_str,
                test_divisible=test_divisible,
                throw_true=throw_true,
                throw_false=throw_false,
                relief_operation=relief_operation
            )

        return monkey
