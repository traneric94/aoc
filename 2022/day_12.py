from collections import deque

def find_cell(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == target:
                return (i, j)
    return -1

def traverse(grid, start_coordinates, end_coordinates):
    levels = {char: i for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
    start_point, end_point = 'S', 'E'
    levels[start_point] = levels['a']
    levels[end_point] = levels['z']


    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    queue = [(0, start_coordinates)]
    visited = set()

    while len(queue) != 0:
        steps, (x, y) = queue.pop(0)

        if (x, y) == end_coordinates:
            return steps
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[nx])):
                continue

            if levels[grid[x][y]] - levels[grid[nx][ny]] < -1:
                continue

            if (nx, ny) in visited:
                continue

            visited.add((nx, ny))

            queue.append((steps + 1, (nx, ny)))

    return float('inf')


def day_one(grid):
    start_coordinates = find_cell(grid, 'S')
    end_coordinates = find_cell(grid, 'E')
    return traverse(grid, start_coordinates, end_coordinates)

def day_two(grid):
    possible_start_coordinates = set()
    end_coordinates = find_cell(grid, 'E')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'a':
                possible_start_coordinates.add((i, j))
    
    result = float('inf')
    for starts in possible_start_coordinates:
        result = min(traverse(grid, starts, end_coordinates), result)
    return result

        

if __name__ == '__main__':
    with open('day_12_input.txt') as f:
        rows = f.readlines()
    
    grid = [row.strip() for row in rows]
    print(day_one(grid))
    print(day_two(grid))
