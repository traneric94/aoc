
# make monkeys

# loop through monkeys
# monkey inspects
# relief // 3
# monkey test
# monkey throw


class Monkey:
    def __init__(self, id, items, operation, test):
        self.id = id
        self.items = items
        self.operation = None # function
        self.test = None # function
        self.inspection_count = 0
    
    # inspects each item in the list
    def inspect_items(self, worry):
        for item in item:
            self.operation(item)
            yield worry
            self.test(item)
            self.inspection_count += 1
    
    def throw(self):
        pass

    def catch(self, item):
        self.append(item)
    
    def __str__(self):
        return f'Monkey {self.id}'
