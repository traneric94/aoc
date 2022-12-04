from collections import Counter


def get_ord(ch):
    if ch.lower() == ch:
        return ord(ch) - ord("a") + 1
    return ord(ch) - 38


def day_one(lines):
    result = 0
    # a => 97, A => 65
    # a => 1, A => 27
    for line in lines:
        mid = int(len(line) / 2)
        for ch in line[mid:]:
            if ch in {*line[:mid]}:
                result += get_ord(ch)
                break

    print("Day 1: %d" % result)


def day_two(lines):
    result = 0

    i = 0
    while i < len(lines):
        union = (
            set(lines[i].strip()).intersection(lines[i + 1]).intersection(lines[i + 2])
        )

        result += get_ord(union.pop())
        i += 3
    print("Day 2: %d" % result)


if __name__ == "__main__":
    with open("day_3_input.txt") as f:
        lines = f.readlines()
        day_one(lines)
        day_two(lines)
