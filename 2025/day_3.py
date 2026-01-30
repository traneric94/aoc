def max_subsequence_value(num_str, length):
    to_remove = len(num_str) - length
    stack = []

    for digit in num_str:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    result_digits = stack[:length]
    return int("".join(result_digits))


def day_3(lines):
    part1 = part2 = 0
    for line in lines:
        part1 += max_subsequence_value(line, 2)
    for line in lines:
        part2 += max_subsequence_value(line, 12)

    print("Day 3: Part 1:", part1)
    print("Day 3: Part 2:", part2)


if __name__ == "__main__":
    with open("day_3_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        day_3(lines)
