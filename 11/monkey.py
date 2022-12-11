from collections import deque

class Monkey:
    other_monkeys = None

    def __init__(self, id, starting_items, operation, test_divisible, throw_true, throw_false, relief_operation=True):
        self.id = id
        self.items = deque(starting_items)
        self.test_divisible = test_divisible
        self.operation = operation
        self.throw_rules = {
            False: throw_false,
            True: throw_true
        }
        self.items_inspected = 0
        self.relief_operation = relief_operation
        self.limit = None

    def __str__(self):
        monkey_str = f"""Monkey #{self.id}
    items: {list(self.items)}
    test dibisible by: {self.test_divisible}
    operation: {self.operation}
    throw to: {self.throw_rules}
    *** items inspected: {self.items_inspected}
        """
        return monkey_str

    def throw_to(self, item, monkey):
        monkey.items.append(item)

    def inspect(self, old):
        # Execute operation
        new = eval(self.operation)
        # Get bored
        if self.relief_operation:
            new = new // 3
        else:
            new = new % self.limit
        # Throw to new monkey
        self.throw_to(new, Monkey.other_monkeys[self.throw_rules[new % self.test_divisible == 0]])
        self.items_inspected += 1

    def process_turn(self):
        while self.items:
            item = self.items.popleft()
            self.inspect(item)
