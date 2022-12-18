def day_one(lines):
    result = 0
    for ranges in lines:
        if ranges[0][1] >= ranges[1][1] or ranges[0][0] == ranges[1][0]:
            result += 1
    print("Day 1: %d" % result)


def day_two(lines):
    result = 0
    for ranges in lines:
        if ranges[0][1] >= ranges[1][0]:
            result += 1
    print("Day 2: %d" % result)


if __name__ == "__main__":
    with open("day_4_input.txt") as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        ranges = line.strip().split(",")
        for idx1, range1 in enumerate(ranges):
            ranges[idx1] = [int(num) for num in range1.split("-")]
        lines[idx] = ranges

        if ranges[0][0] > ranges[1][0]:
            ranges[0], ranges[1] = ranges[1], ranges[0]

    day_one(lines)
    day_two(lines)
