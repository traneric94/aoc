def day_one(stacks, commands):
    for command in commands:
        stacks[command[2]][:0] = stacks[command[1]][: command[0]][::-1]
        stacks[command[1]] = stacks[command[1]][command[0] :]

    result = ""
    for stack in stacks:
        result += stack[0]

    print("Day 1: %s" % result)


def day_two(stacks, commands):
    for command in commands:
        stacks[command[2]][:0] = stacks[command[1]][: command[0]]
        stacks[command[1]] = stacks[command[1]][command[0] :]

    result = ""
    for stack in stacks:
        result += stack[0]

    print("Day 2: %s" % result)


def parse_stacks(lines):
    supply_stacks = []
    x = 1
    while x < len(lines[0]):
        stack = []
        for line in lines:
            stack.append(line[x]) if line[x] != " " else None
        supply_stacks.append(stack)
        x += 4
    return supply_stacks


def parse_commands(lines):
    commands = []
    for line in lines:
        remove_move = line.strip().split("move")
        remove_from = remove_move.pop().split("from")
        remove_to = remove_from.pop().split("to")

        command = [
            int(*remove_from),
            int(remove_to[0]) - 1,
            int(remove_to[1]) - 1,
        ]

        commands.append(command)

    return commands


if __name__ == "__main__":
    with open("day_5_input.txt") as f:
        lines = f.readlines()

    commands = parse_commands(lines[10:])
    stacks = parse_stacks(lines[:8])

    day_one([stack[:] for stack in stacks], commands)
    day_two([stack[:] for stack in stacks], commands)
