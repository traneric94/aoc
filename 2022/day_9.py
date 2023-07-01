import math

direction_map = {
    'R': [1, 0],
    'U': [0, 1],
    'L': [-1, 0],
    'D': [0, -1],
}

def distance(point1, point2):
    return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))


def apply_direction(position, direction):
    return [sum(x) for x in zip(position, direction)]

def update_tail_position(head_position, tail_position):
    if distance(head_position, tail_position) < 2:
        return tail_position
    if head_position[0] == tail_position[0]:
        tail_position[1] = int((head_position[1] + tail_position[1]) / 2)
    elif head_position[1] == tail_position[1]:
        tail_position[0] = int((head_position[0] + tail_position[0]) / 2)
    else:
        x_direction = head_position[0] - tail_position[0]
        y_direction = head_position[1] - tail_position[1]

        if x_direction > 0:
            tail_position[0] += 1
        else:
            tail_position[0] -= 1

        if y_direction > 0:
            tail_position[1] += 1
        else:
            tail_position[1] -= 1

    return tail_position

def day_one(instructions):
    tail_positions = set() # (x, y), set of x,y visited coordinates
    head_position = [0,0] 
    tail_position = [0,0]

    for direction, magnitude in instructions:
        
        while magnitude > 0:
            head_position = apply_direction(head_position, direction_map[direction])
            tail_position = update_tail_position(head_position, tail_position)
            tail_positions.add(tuple(tail_position))
            magnitude -= 1
    print(f"Day 1: {len(tail_positions)}")            

def day_two(instructions):
    visited = set()
    positions = [ [0,0] for _ in range(10)]
    for direction, magnitude in instructions:
        while magnitude > 0:
            positions[0] = apply_direction(positions[0], direction_map[direction])
            for index in range(1, 10):
                positions[index] = update_tail_position(positions[index-1], positions[index])
            visited.add(tuple(positions[9]))
            magnitude -= 1
    print(f"Day 2: {len(visited)}")            




if __name__ == '__main__':
    with open('day_9_input.txt') as f:
        lines = f.readlines()

    instructions = []

    for line in lines:
        direction, magnitude = line.split(' ')
        magnitude_int = int(magnitude)
        instructions.append([direction, magnitude_int])


    day_one(instructions)
    day_two(instructions)
