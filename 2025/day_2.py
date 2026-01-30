from bisect import bisect_left, bisect_right


def day_2(ranges):
    parsed = []
    upper_limit = 0
    for r in ranges:
        start, end = r.split("-")

        start = int(start)
        end = int(end)

        upper_limit = max(upper_limit, end)

        parsed.append((int(start), int(end)))

    twice_nums, twice_prefix = build_repeated_numbers(
        upper_limit,
        min_repeat=2,
        max_repeat=2,
    )
    repeat_nums, repeat_prefix = build_repeated_numbers(
        upper_limit,
        min_repeat=2,  # min_repeat
    )

    part_1 = part_2 = 0
    for start, end in parsed:
        part_1 += range_sum(twice_nums, twice_prefix, start, end)
        part_2 += range_sum(repeat_nums, repeat_prefix, start, end)

    print("Day 2: Part 1:", part_1)
    print("Day 2: Part 2:", part_2)


def range_sum(nums, prefix_sums, start, end):
    if not nums or start > end:
        return 0
    left = bisect_left(nums, start)
    right = bisect_right(nums, end)

    return prefix_sums[right] - prefix_sums[left]


def build_repeated_numbers(upper_limit, min_repeat=2, max_repeat=None):
    if upper_limit < 0:
        return [], [0]

    max_digits = len(str(upper_limit))
    if max_digits == 0:
        return [], [0]

    repeat_upper = max_repeat if max_repeat is not None else max_digits
    repeat_upper = min(repeat_upper, max_digits)

    repeated_numbers = set()

    for repeat in range(min_repeat, repeat_upper + 1):
        max_pattern_len = max_digits // repeat
        if max_pattern_len == 0:
            break

        for pattern_len in range(1, max_pattern_len + 1):
            start = 10 ** (pattern_len - 1)
            end = 10 ** pattern_len

            for pattern in range(start, end):
                pattern_str = str(pattern)
                value = int(pattern_str * repeat)
                if value > upper_limit:
                    break

                repeated_numbers.add(value)

    numbers = sorted(repeated_numbers)
    prefix_sums = [0]
    for num in numbers:
        prefix_sums.append(prefix_sums[-1] + num)

    return numbers, prefix_sums


if __name__ == "__main__":
    with open("day_2_input.txt") as f:
        lines = f.readlines()[0].split(",")

    ranges = [line.strip() for line in lines]

    day_2(ranges)
