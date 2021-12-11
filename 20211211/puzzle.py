#%%
import numpy as np
import csv

data = []

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        data.append(list(map(int, list(line[0]))))

data = np.array(data)


def find_neighbors(index, arr):
    x, y = index
    possible = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]

    print(
        list(
            filter(
                lambda i: bool(map(lambda a, b: a > b, i, (0, 0)))
                & bool(map(lambda a, b: a < b, i, arr.shape)),
                possible,
            )
        )
    )


find_neighbors((0, 0), data)
