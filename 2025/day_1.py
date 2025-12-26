def day_1(lines):
    dial_pointer = 50
    counter = 0
    for line in lines:

        dial_pointer += line
        dial_pointer %= 100

        if dial_pointer == 0:
            counter += 1
    print("count", counter)


def day_2(turns):
    dial_pointer = 50
    counting = 0

    for turn in turns:

        if turn < 0:
            amount_to_first_turn = dial_pointer % 100
        else:
            amount_to_first_turn = (100 - dial_pointer) % 100

        if amount_to_first_turn == 0:
            amount_to_first_turn = 100

        dial_pointer += turn
        dial_pointer %= 100

        turn = abs(turn)

        if turn >= amount_to_first_turn:
            counting += 1 + (turn - amount_to_first_turn) // 100

    print("count", counting)


def test(lines):
    pos = 50
    p1 = 0
    p2 = 0

    for line in lines:
        d = line[0]
        amt = int(line[1:])

        for _ in range(amt):
            if d == "L":
                pos = (pos - 1 + 100) % 100
            else:
                pos = (pos + 1) % 100

            if pos == 0:
                p2 += 1

        if pos == 0:
            p1 += 1

    print(p1)
    print(p2)


if __name__ == "__main__":
    with open("Day_1_input.txt") as f:
        # print("test", test(f.readlines()))
        lines = list(map(int, f.read().replace("R", "").replace("L", "-").split()))

    print("Day 1, Part 1")
    day_1(lines)
    print("Day 1, Part 2")
    day_2(lines)
