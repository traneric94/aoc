import json

class Pair:
    def __init__(self, left, right):
        self.left = json.loads(left)
        self.right = json.loads(right)
    
    def __str__(self):
        return f'L:{self.left} R: {self.right}'

def compare(left, right):
    print(left, right)
    # checking 0
    # correct 1
    # incorrect 2

    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left > right:
                return 2
        else:
            return 0
    
    if type(left) == list and type(right) == list:
        i, j = 0, 0
        while i < len(left) or j < len(right):
            if i < len(left) and j < len(right):
                result = compare(left[i], right[j])
                if result != 0:
                    return result
            
            elif i < len(left):
                return 2
            elif j < len(right):
                return 1
            i += 1
            j += 1
    
    if type(left) != list:
        return compare([left], right)
    if type(right) != list:
        return compare(left, [right])
    
    print(left, right, 'HOW')
    return 1

def day_one(pairs):
    result = []
    values = []
    for i, pair in enumerate(pairs):
        values.append(compare(pair.left, pair.right))
        if compare(pair.left, pair.right) == 1:
            result.append(i)
    
    # print(sum(result), result)
    print(values)
    print([1, 1, 2, 1, 2, 1, 2, 2])
    return result


if __name__ == '__main__':
    with open('day_13_input.txt') as f:
        rows = f.readlines()
    
    pairs = []
    i = 0
    while i < len(rows):
        pairs.append(Pair(rows[i].strip(), rows[i+1].strip()))
        i += 3

    day_one(pairs)
