def day_4(matrix):
    r1, r2 = 0, 0
    adj = [
        [1, 0],
        [0, 1],
        [1, 1],
        [-1, 0],
        [0, -1],
        [-1, -1],
        [1, -1],
        [-1, 1],
    ]

    queue = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@":
                if has_rolls(matrix, i, j, 4):
                    r1 += 1
                    queue.append((i, j))

    while len(queue) != 0:
        i, j = queue.pop()

        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
            continue

        if matrix[i][j] == "@" and has_rolls(matrix, i, j, 4):
            matrix[i][j] = "x"

            r2 += 1

            for di, dj in adj:
                queue.append((i + di, j + dj))

    print("Day 4: Part 1", r1)
    print("Day 4: Part 2", r2)


def has_rolls(matrix, i, j, required_count) -> bool:
    adj = [
        [1, 0],
        [0, 1],
        [1, 1],
        [-1, 0],
        [0, -1],
        [-1, -1],
        [1, -1],
        [-1, 1],
    ]
    count = 0
    for di, dj in adj:
        ni, nj = i + di, j + dj

        if ni < 0 or ni >= len(matrix):
            continue
        if nj < 0 or nj >= len(matrix[i]):
            continue

        if matrix[ni][nj] == "@":
            count += 1

    return count < required_count


if __name__ == "__main__":
    with open("day_4_input.txt") as f:
        lines = [list(line) for line in f.readlines()]

    day_4(lines)
