def day_one(stream):
    result = find_substr_in_stream(stream, 4)
    print(f"Day 1: %d", result)


def day_two(stream):
    result = find_substr_in_stream(stream, 14)
    print(f"Day 2: %d", result)


def find_substr_in_stream(stream, marker_length):
    idx = 0
    while idx < len(stream):
        if len(set(stream[idx : idx + marker_length])) == marker_length:
            return idx + marker_length
        idx += 1


if __name__ == "__main__":
    with open("day_6_input.txt") as f:
        lines = f.readlines()
    day_one(lines[0])
    day_two(lines[0])
