

def day_one(lines):
    signal_strengths = []
    num_cycles = 0
    x = 1
    for line in lines:
        instruction = line.strip()
        num_cycles += 1
        if (num_cycles % 40) - 20 == 0:
            signal_strengths.append(x * num_cycles)
        if instruction != 'noop':
            num_cycles += 1
            if (num_cycles % 40) - 20 == 0:
                signal_strengths.append(x * num_cycles)
            _, num = instruction.split(' ')
            x += int(num)

    print(f'Day One: {sum(signal_strengths)}')

def check_cycle_and_x(cycle, x):
    cycle = cycle % 40 + 1
    if cycle - 2 <= x <= cycle:
        return '#', cycle
    else:
        return '.', cycle
        
def day_two(lines):
    x = 1
    cycle = 0
            
    for line in lines:
        instruction = line.strip()

        pixel, cycle = check_cycle_and_x(cycle, x)
        yield pixel 

        if instruction != 'noop':
            _, num = instruction.split(' ')
            pixel, cycle = check_cycle_and_x(cycle, x)
            yield pixel 
            x += int(num)

if __name__ == '__main__':
    with open('day_10_input.txt') as f:
        lines = f.readlines()

    day_one(lines)

    result = list(day_two(lines))
    j = 0
    while j < len(result):
        print(''.join(result[j:j+40]))
        j += 40
