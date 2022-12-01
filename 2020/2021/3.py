from Day_1 import get_product

def parseMatrix(lines):
    return list(map(lambda x: [c for c in x], lines))

def countTrees(matrix, rightward, downward):
    position = [0,0]
    num_trees = 0
    while position[0] < len(matrix):
        print(matrix[position[0]][position[1]])
        if matrix[position[0]][position[1]] == '#':
            num_trees += 1
        position[0] += downward
        position[1] = (position[1] + rightward) % (len(matrix[0]) - 1)
    return num_trees

if __name__ == '__main__':
    with open('Day_3_input.txt') as f:
        lines = f.readlines()
        matrix = parseMatrix(lines)

        results = []
        results.append(countTrees(matrix, 1, 1))
        results.append(countTrees(matrix, 3, 1))
        results.append(countTrees(matrix, 5, 1))
        results.append(countTrees(matrix, 7, 1))
        results.append(countTrees(matrix, 1, 2))
        print(results)
        print('product', get_product(results))
    
