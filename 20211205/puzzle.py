#%%
import pandas as pd
import numpy as np

# Part 1
data = pd.read_csv("input.csv", delimiter=" -> ")


def str_to_tuple(row):
    _from = np.array([int(i) for i in row["from"].split(",")])
    _to = np.array([int(i) for i in row["to"].split(",")])
    _diff = _from - _to
    if _diff[0] == 0:
        _y = [_from[_diff != 0][0], _to[_diff != 0][0]]
        _x = _to[_diff == 0][0]
        rng = list(range(min(_y), max(_y) + 1))
        return pd.Series([_from, _to, _diff, _x, rng, max(np.max(_from), np.max(_to))])
    if _diff[1] == 0:
        _x = [_from[_diff != 0][0], _to[_diff != 0][0]]
        _y = _to[_diff == 0][0]
        rng = list(range(min(_x), max(_x) + 1))
        return pd.Series([_from, _to, _diff, rng, _y, max(np.max(_from), np.max(_to))])

    return pd.Series([_from, _to, _diff, None, None, None])


data[["from", "to", "diff", "x", "y", "max"]] = data.apply(str_to_tuple, axis=1)

board = np.zeros((int(data["max"].max() + 1), int(data["max"].max() + 1)))

for i, row in data.iterrows():
    if row["x"] or row["y"]:
        board[row["y"], row["x"]] += 1

print(board)
print(np.sum(board > 1))


# Part 2
data = pd.read_csv("input.csv", delimiter=" -> ")


def str_to_tuple(row):
    _from = np.array([int(i) for i in row["from"].split(",")])
    _to = np.array([int(i) for i in row["to"].split(",")])
    _diff = _from - _to

    x_min = min(_from[0], _to[0])
    x_max = max(_from[0], _to[0])
    y_min = min(_from[1], _to[1])
    y_max = max(_from[1], _to[1])

    y, x = range(y_min, y_max + 1), range(x_min, x_max + 1)  # base case

    if _diff[0] == 0:  # same x axis
        x = [x_min] * (y_max - y_min + 1)
    if _diff[1] == 0:  # same y axis
        y = [y_min] * (x_max - x_min + 1)

    if (_from[0] > _to[0]) & (0 not in _diff):  # reverse x if to is lower than from
        x = list(reversed(range(x_min, x_max + 1)))
    if (_from[1] > _to[1]) & (0 not in _diff):  # reverse y if to is lower than from
        y = list(reversed(range(y_min, y_max + 1)))

    mark = [y, x]
    return pd.Series([_from, _to, mark, max(np.max(_from), np.max(_to))])


data[["from", "to", "mark", "max"]] = data.apply(str_to_tuple, axis=1)

board = np.zeros((int(data["max"].max() + 1), int(data["max"].max() + 1)))

for i, row in data.iterrows():
    board[row["mark"]] += 1

print(board)
print(np.sum(board > 1))


# %%
