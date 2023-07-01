

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

def day_two(lines):
    result = []
    cycle = 0
    x = 1
    for line in lines:
        instruction = line.strip()
        cycle += 1
        if cycle - 1 <= x <= cycle + 1:
            result.append('#')
        else:
            result.append('.')
        if instruction != 'noop':
            cycle += 1
            _, num = instruction.split(' ')
            x += int(num) 
    
    
    for index, ch in enumerate(result):
        print(ch + '\n') if index == 20 else print(ch)







if __name__ == '__main__':
    with open('day_10_input.txt') as f:
        lines = f.readlines()

    day_one(lines)
    day_two(lines)
