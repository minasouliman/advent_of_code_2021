#%%
import numpy as np
import csv

from numpy.core.fromnumeric import shape

data = []

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        data.append(list(map(int, list(line[0]))))

data = np.array(data)


data_y = np.diff(data)
data_x = np.diff(data, axis=0)

data_rev = np.flip(data, axis=1)
data_y_rev = np.diff(data_rev)
data_rev = np.flip(data, axis=0)
data_x_rev = np.diff(data_rev, axis=0)

all = np.array((data, data_x, data_x_rev, data_y, data_y_rev))

data_y = data_y < 0
data_y = np.insert(data_y, 0, True, axis=1)
data_x = data_x < 0
data_x = np.insert(data_x, 0, True, axis=0)

data_x_rev = data_x_rev < 0
data_x_rev = np.flip(data_x_rev, axis=0)
data_x_rev = np.insert(data_x_rev, data_x_rev.shape[0], True, axis=0)

data_y_rev = data_y_rev < 0
data_y_rev = np.flip(data_y_rev, axis=1)
data_y_rev = np.insert(data_y_rev, data_y_rev.shape[1], True, axis=1)


all = np.array((data_x, data_x_rev, data_y, data_y_rev))
sinks = np.logical_and.reduce(all)
# print(sum(data[sinks] + 1))


# Part 2, copied from https://www.reddit.com/r/adventofcode/comments/rca6vp/2021_day_9_solutions/?sort=top, couldn't get myself to spend more time on it

sinks = dict(np.ndenumerate(sinks))
sink_keys = [key for key in sinks if sinks[key] == True]
data = dict(np.ndenumerate(data))


def neighbours(x, y):
    return filter(
        lambda n: n in data,  # remove points
        [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)],
    )  #  outside grid


def count_basin(p):
    if data[p] == 9:
        return 0  # stop counting at ridge
    del data[p]  # prevent further visits
    return 1 + sum(map(count_basin, neighbours(*p)))


basins = [count_basin(p) for p in sink_keys]
print(np.prod(sorted(basins)[-3:]))
