#%%
import numpy as np
import csv

data = []

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        data.append(list(map(int, list(line[0]))))

data = np.array(data)
SHAPE = np.array(data.shape)
ZEROS = np.array((0, 0))


def find_neighbors(index, arr):
    x, y = index
    potential = np.array(
        [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]
    )

    possible = potential[((potential < SHAPE) & (potential >= ZEROS)).all(axis=1)]
    return possible if len(possible) > 0 else None


flashes = []
for i in range(300):
    flashed = np.zeros(SHAPE, dtype=bool)
    data += 1
    new_flash = data > 9
    flashed = flashed | new_flash
    new_flash_idx = list(zip(*np.where(new_flash == True)))

    while len(new_flash_idx) > 0:
        idx = new_flash_idx[0]
        new_flash_idx.remove(idx)

        neighbors = find_neighbors(idx, data)

        if neighbors.any():
            data[tuple(zip(*neighbors))] += 1
            new_flash = (data > 9) & np.invert(flashed)
            new_flash_idx.extend(
                list(map(tuple, neighbors[new_flash[tuple(zip(*neighbors))]]))
            )
            flashed = flashed | new_flash

    data[data > 9] = 0
    if (data == 0).all():
        print(i + 1)

    flashes.append(np.sum(flashed, axis=None))

print(sum(flashes))


from scipy import signal

convolve_matrix = np.ones((3, 3))
test_matrix = np.array(
    [[False, False, False], [False, False, False], [False, False, False]]
)
neighbour_flashes = (
    signal.convolve(flashes, convolve_matrix, mode="same").round(0).astype(int)
)
