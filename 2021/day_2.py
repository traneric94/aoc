import ntpath

def get_result():
    horizontal_position = 0
    vertical_position = 0
    aim = 0
    with open('day_2_input.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        direction, magnitude = line.split(' ')
        if direction == 'forward':
            vertical_position += aim * int(magnitude)
            horizontal_position += int(magnitude)
        elif direction == 'down':
            aim += int(magnitude)
        elif direction == 'up':
            aim -= int(magnitude)
    return horizontal_position * vertical_position

if __name__ == '__main__':
    print(get_result())
