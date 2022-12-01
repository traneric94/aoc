from functools import reduce

with open('Day_1_input.txt') as f:
    lines = f.readlines()
input = list(map(int, lines))

# Find target sum and product
def find_two_sum(target, nums=input):
    seen = set()
    print('what', len(nums)) 
    for num in nums:
        compliment = target - num
        if (compliment in seen):
            return [num, compliment]
        seen.add(num)

def get_product(nums):
    return reduce((lambda a, b: a * b), nums)

def find_three_sum(target):
    result = []
    seen = {}

    # Generate sum map
    for idx1, num1 in enumerate(input):
        for idx2, num2 in enumerate(input):
            if idx1 == idx2:
                continue
            two_sum = num1 + num2
 
            if seen.get(two_sum, None) is None:
                seen[two_sum] = [[num1,num2]] 
            else:
                seen[two_sum].append([num1, num2])

    
    for num in input:
        compliment = target - num
        if (compliment in seen):
            return [num, *seen[compliment][0]]
    

    addends = find_two_sum(target, list(seen.keys()) + input)
    print(seen.keys())
    print('intermediate addends', addends)
    # grab first
    first_two = seen[addends[0]][0]

    return [*first_two, addends[1]]

if __name__ == "__main__":
    print("Day 1, Part 1")
    addends = find_two_sum(2020)
    print("addends", addends)
    product = get_product(addends)
    print("result", product)
    assert product == 1018336, "result is incorrect"
    print("Passed Day 1, Part 1")

    print("Day 2, Part 2")
    addends = find_three_sum(2020)
    print("addends", addends)
    product = get_product(addends)
    print("result", product)
    print("Passed Day 1, Part 2")
