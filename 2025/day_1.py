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


if __name__ == "__main__":
    with open("Day_1_input.txt") as f:
        lines = list(map(int, f.read().replace("R", "").replace("L", "-").split()))

    print("Day 1, Part 1")
    day_1(lines)
    print("Day 1, Part 2")
    day_2(lines)
    answer(lines)
