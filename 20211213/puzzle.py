#%%

import numpy as np
import csv

np.set_printoptions(
    linewidth=100000,
)
data = []

max_x = 0
max_y = 0
with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        y, x = map(int, line[0].split(","))
        max_x = np.max([max_x, x])
        max_y = np.max([max_y, y])
        data.append((x, y))

data = np.array(data)
arr = np.zeros((max_x + 1, max_y + 1))
arr[data[:, 0], data[:, 1]] = 1


def fold(line, axis, arr):

    if axis == "y":
        fwd = arr[:line, :]
        rev = np.flip(arr[line + 1 :, :], 0)
        if fwd.shape[0] > rev.shape[0]:
            rev = np.insert(
                rev, 0, np.zeros((fwd.shape[0] - rev.shape[0], fwd.shape[1])), axis=0
            )
        elif fwd.shape[0] < rev.shape[0]:
            fwd = np.insert(
                fwd, 0, np.zeros((rev.shape[0] - fwd.shape[0], rev.shape[1])), axis=0
            )

        return fwd + rev
    else:
        fwd = arr[:, :line]
        rev = np.flip(arr[:, line + 1 :], 1)
        if fwd.shape[1] > rev.shape[1]:
            rev = np.insert(
                rev, 0, np.zeros((fwd.shape[0], fwd.shape[1] - rev.shape[1])), axis=1
            )
        elif fwd.shape[1] < rev.shape[1]:
            fwd = np.insert(
                fwd, 0, np.zeros((rev.shape[1] - fwd.shape[1], rev.shape[0])), axis=1
            )
        return fwd + rev


folds = [
    (655, "x"),
    (447, "y"),
    (327, "x"),
    (223, "y"),
    (163, "x"),
    (111, "y"),
    (81, "x"),
    (55, "y"),
    (40, "x"),
    (27, "y"),
    (13, "y"),
    (6, "y"),
]
# folds = [(7,'y'),(5,'x')]
for _f in folds:
    arr = fold(_f[0], _f[1], arr)
    print(arr.shape)

arr[arr >= 1] = 1
print(arr)
# np.sum(arr>=1)
# %%
