import random

# KD tree
# quick select median, pivot until we get the kth at each level
# n log n to build the tree
# rotate dimensions at each level
# search algorithm to find the nearest

with open("day_8_input.txt") as f:
    points = [tuple(int(a) for a in line.strip().split(",")) for line in f]


def children(i):
    return (i * 2, i * 2 + 2)


def parent(i):
    return (i - 1) // 2


def level(i):
    return (i + 1).bit_length() - 1


def qs(nums):
    mid = len(nums) // 2
    pivot = random.randint(0, len(nums))
    left, right = [], []
