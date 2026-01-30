from functools import cache

with open("day_7_input.txt") as f:
    m = [line.strip() for line in f.readlines()]


beam = {"count": 0}
hit = set()


@cache
def split(i, j):
    if i >= len(m) or j < 0 or j >= len(m[0]):
        return

    if i == len(m) - 1:
        return

    if m[i][j] == "^":
        if (i, j) not in hit:
            beam["count"] += 1
            hit.add((i, j))

        split(i + 1, j + 1)
        split(i + 1, j - 1)
        return

    split(i + 1, j)


s = m[0].find("S")
split(0, s)


print("Day 7: Part 1", beam)


hit_2 = set()


@cache
def split_2(i, j):
    if i >= len(m) or j < 0 or j >= len(m[0]):
        return 1

    if m[i][j] == "^":
        if (i, j) not in hit_2:
            hit_2.add((i, j))
            return split_2(i + 1, j + 1) + split_2(i + 1, j - 1)

    return split_2(i + 1, j)


print("Day 7: Part 2", split_2(0, s))
