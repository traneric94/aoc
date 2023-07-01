def populate_result(temp, tree_rows):
    for i in range(len(tree_rows)):
        temp[i][0]['W'] = tree_rows[i][0] # west side
        temp[i][0]['is_visible'] = True
        temp[i][len(tree_rows)-1]['E']  = tree_rows[i][len(tree_rows)-1]# east
        temp[i][len(tree_rows)-1]['is_visible'] = True

    for i in range(len(tree_rows[0])):
        temp[0][i]['N'] = tree_rows[0][i] # north
        temp[0][i]['is_visible'] = True
        temp[len(tree_rows)-1][i]['S'] = tree_rows[len(tree_rows)-1][i] # south
        temp[len(tree_rows)-1][i]['is_visible'] = True

def day_one(rows):
    result = [[{'N': 0, 'S': 0, 'W': 0, 'E': 0, 'is_visible': False} for _ in row] for row in tree_rows]

    populate_result(result, rows)

    for i in range(1, len(rows)):
        for j in range(1, len(rows[i])):

            result[i][j]['W'] = max(result[i][j-1]['W'], rows[i][j])

            if result[i][j - 1]['W'] < rows[i][j]:
                result[i][j]['is_visible'] = True
            
            result[i][j]['N'] = max(result[i-1][j]['N'], rows[i][j])

            if result[i-1][j]['N'] < rows[i][j]:
                result[i][j]['is_visible'] = True
    
    for i in reversed(range(0, len(rows) - 1)):
        for j in reversed(range(0, len(rows[i]) - 1)):

            result[i][j]['E'] = max(result[i][j+1]['E'], rows[i][j])

            if result[i][j+1]['E'] < rows[i][j]:
                result[i][j]['is_visible'] = True

            result[i][j]['S'] = max(result[i+1][j]['S'], rows[i][j])

            if result[i+1][j]['S'] < rows[i][j]:
                result[i][j]['is_visible'] = True
    
    visibility_count = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if result[i][j]['is_visible']:
                visibility_count += 1
    print(f"Day 1: {visibility_count}")

def day_two(rows):
    # bloom out from a point for each one
    def is_in_bounds(rows, new_coordinates):
        return new_coordinates[0] < len(rows) and \
                new_coordinates[0] >= 0 and \
                new_coordinates[1] >= 0 and \
                new_coordinates[1] < len(rows[0])
        
    result = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            scenery_score = 1
            for increment in ([0,1], [1,0], [-1,0], [0,-1]):
                distance = 0
                new_coordinates = [i, j]
                while True:
                    print(new_coordinates, increment)
                    new_coordinates = [new_coordinates[0] + increment[0], new_coordinates[1] + increment[1]]
                    if not is_in_bounds(rows, new_coordinates):
                        break
                    if rows[i][j] >= rows[new_coordinates[0]][new_coordinates[1]]:
                        distance += 1
                    if rows[i][j] == rows[new_coordinates[0]][new_coordinates[1]]:
                        break
                scenery_score *= distance
            result = max(scenery_score, result)
            
    print(f"Day 2: {result}")


def parse_input(lines):
    result = []
    for line in lines:
        result.append([int(x) for x in line.strip()])
    return result


if __name__ == "__main__":
    with open("day_8_input.txt") as f:
        lines = f.readlines()

    tree_rows = parse_input(lines)
    day_one(tree_rows)
    day_two(tree_rows)
