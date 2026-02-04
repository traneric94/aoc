from math import sqrt, inf


def load(path="day_8_input.txt"):
    with open(path) as f:
        return [tuple(map(int, ln.strip().split(","))) for ln in f if ln.strip()]


def dist(a, b):
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


points = load()

nearest = (inf, None, None)
for i in range(len(points)):
    for j in range(len(points)):
        if i == j:
            continue
connected_sets = []
