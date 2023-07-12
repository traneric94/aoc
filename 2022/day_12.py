from collections import deque

def day_one(grid):
    levels = {char: i for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
    levels['S'] = levels['a']
    levels['E'] = levels['z']
   # Start and end points
    start_point, end_point = 'S', 'E'

    # Find start and end coordinates
    start_coordinates, end_coordinates = None, None

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == start_point:
                start_coordinates = (i, j)
            if grid[i][j] == end_point:
                end_coordinates = (i, j)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    queue = [(0, start_coordinates)]
    visited = set()

    while len(queue) != 0:
        steps, (x, y) = queue.pop()

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

    return -1

if __name__ == '__main__':
    with open('day_12_input.txt') as f:
        rows = f.readlines()
    
    grid = [row.strip() for row in rows]
    print(day_one(grid))
