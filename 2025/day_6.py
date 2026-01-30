from math import prod

# group
# iterate by col then row
# if all whitespace; new group continue


# accrue digits vertically in a list
# then execute operator


with open("day_6_input.txt") as f:
    m = [line for line in f.readlines()]

op_row = len(m) - 1
for x in m:
    print(x)
ng = []
nums = []
for j, _ in enumerate(m[0]):
    num = []
    for i, _ in enumerate(m):
        if all(x[j] == " " or x[j] == "\n" for x in m):
            if nums:
                ng.append(nums)
            nums = []
            continue

        if i == op_row:
            nums.append(int("".join(num)))

        if m[i][j] in "+*":
            nums.insert(0, m[i][j])
            continue

        num.append(m[i][j])

r2 = 0
for op, *nums in ng:
    r = 0
    if op == "*":
        r = prod(nums)
    else:
        r = sum(nums)
    print(r, nums)
    r2 += r

print("Day 6: Part 2", r2)
