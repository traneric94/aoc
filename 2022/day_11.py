import re

def parse_id(s): 
    return int(s.split()[-1][:-1])

def parse_items(item_str):
    _, items = item_str.strip().split(':')
    return [int(x) for x in items.split(',')]

def parse_operation(operation_str):
    _, operation = operation_str.strip().split('= ')
    return operation

def parse_int(s):
    return int(re.search(r'\d+', s).group())

class Monkey:
    def __init__(self, *args):
        self.id = parse_int(args[0])
        self.items = parse_items(args[1])
        self.operation = parse_operation(args[2])
        self.test = parse_int(args[3])
        self.success_monkey = parse_int(args[4])
        self.fail_monkey = parse_int(args[5])
        self.inspection_count = 0
    
    # inspects each item in the list
    def inspect_items(self, test_product):
        while self.items:
            item = self.items.pop(0)
            new_item = self.call_operation(item)
            new_item %= test_product
            
            if new_item % self.test == 0:
                yield new_item, self.success_monkey
            else:
                yield new_item, self.fail_monkey

            self.inspection_count += 1
            
    def call_operation(self, old):
        return eval(self.operation)
    
    def __str__(self):
        return f'Monkey {self.id}: Inspected {self.inspection_count} items.'
        # return f'Monkey {self.id}: {len(self.items)}' if len(self.items) > 0 else ''

def day_one(monkeys):
    test_product = 1
    for monkey in monkeys:
        test_product *= monkey.test

    for i in range(10000):
        for monkey in monkeys:
            for item, catching_monkey in monkey.inspect_items(test_product):
                monkeys[catching_monkey].items.append(item)
    
    for monkey in monkeys:
        print(monkey)


if __name__ == '__main__':
    with open('day_11_input.txt') as f:
        rows = f.readlines()

    monkeys = []
    i = 0
    while i < len(rows):
        monkeys.append(Monkey(*rows[i:i+6]))
        i += 7
    
    day_one(monkeys)
