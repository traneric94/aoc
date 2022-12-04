map = {
    "A": 1,  # rock
    "X": 1,  # rock
    "B": 2,  # paper
    "Y": 2,  # paper
    "C": 3,  # scissors
    "Z": 3,  # scissors
}

wins = {3: 1, 1: 2, 2: 3}
losses = {v: k for k, v in wins.items()}
draws = {k: k for k, _ in wins.items()}


def day_one(lines):
    result = 0
    for line in lines:
        a, b = line.split()
        if map[a] == map[b]:
            result += 3
        elif wins[map[a]] == map[b]:
            result += 6
        result += map[b]

    print("day 1: %d" % result)  # 11386


def day_two(lines):
    counter = {
        "Y": draws,
        "X": losses,
        "Z": wins,
    }
    outcome = {
        "Y": 3,
        "X": 0,
        "Z": 6,
    }

    result = 0
    for line in lines:
        a, b = line.split()
        result += counter[b][map[a]]  # gets me the value
        result += outcome[b]

    print("day 2: %d" % result)


if __name__ == "__main__":
    with open("day_2_input.txt") as f:
        lines = f.readlines()
        day_one(lines)
        day_two(lines)
