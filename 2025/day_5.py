from bisect import bisect_left, bisect_right

if __name__ == "__main__":
    with open("day_5_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    ranges = []
    nums = []

    i = 0
    while lines[i] != "":
        ranges.append(lines[i])
        i += 1

    i += 1

    while i < len(lines):
        nums.append(int(lines[i]))
        i += 1

    for i in range(len(ranges)):
        s, e = ranges[i].split("-")
        ranges[i] = (int(s), int(e))

    ranges.sort(key=lambda x: (x[0], x[1]))

    merged_ranges = [ranges.pop(0)]

    i = 0
    while i < len(ranges):
        s, e = ranges[i]

        if merged_ranges[-1][1] >= s:
            merged_ranges[-1] = (
                min(merged_ranges[-1][0], ranges[i][0]),
                max(merged_ranges[-1][1], ranges[i][1]),
            )
        else:
            merged_ranges.append(ranges[i])

        i += 1

    # binary search for interval, lets use bisect
    starts = [r[0] for r in merged_ranges]
    r1 = 0
    for num in nums:
        i = bisect_left(starts, num)
        if i == 0:
            continue
        # we need to check just interval before end
        if merged_ranges[i - 1][1] >= num:
            r1 += 1

    # Day 2
    r2 = 0
    for r in merged_ranges:
        r2 += r[1] - r[0] + 1

    print("Day 5: Part 1", r1)
    print("Day 5: Part 2", r2)
