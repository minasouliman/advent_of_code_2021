#%%
import pandas as pd
import numpy as np

draws = [
    85,
    84,
    30,
    15,
    46,
    71,
    64,
    45,
    13,
    90,
    63,
    89,
    62,
    25,
    87,
    68,
    73,
    47,
    65,
    78,
    2,
    27,
    67,
    95,
    88,
    99,
    96,
    17,
    42,
    31,
    91,
    98,
    57,
    28,
    38,
    93,
    43,
    0,
    55,
    49,
    22,
    24,
    82,
    54,
    59,
    52,
    3,
    26,
    9,
    32,
    4,
    48,
    39,
    50,
    80,
    21,
    5,
    1,
    23,
    10,
    58,
    34,
    12,
    35,
    74,
    8,
    6,
    79,
    40,
    76,
    86,
    69,
    81,
    61,
    14,
    92,
    97,
    19,
    7,
    51,
    33,
    11,
    77,
    75,
    20,
    70,
    29,
    36,
    60,
    18,
    56,
    37,
    72,
    41,
    94,
    44,
    83,
    66,
    16,
    53,
]

import pandas as pd

data = pd.read_csv("input.csv")


def str_to_list(row):
    return row.str.split()


data = data.apply(str_to_list, axis=0)
data = pd.DataFrame(data.Rows.tolist(), index=data.index)
data = data.apply(pd.to_numeric)

num_of_boards = int(len(data) / 5)
boards = np.reshape(data.values, (num_of_boards, 5, 5))

for i in range(len(draws)):
    state = np.isin(boards, draws[:i])
    columns = state.all(axis=1).any(axis=1)
    rows = state.all(axis=2).any(axis=1)
    if columns.any():
        called = np.isin(boards[columns], draws[:i])
        print(np.sum(boards[columns][~called]), draws[i - 1])
        break

    if rows.any():
        called = np.isin(boards[rows], draws[:i])
        print(np.sum(boards[rows][~called]), draws[i - 1])
        break

for i in range(len(draws)):
    state = np.isin(boards, draws[:i])
    columns = state.all(axis=1).any(axis=1)
    rows = state.all(axis=2).any(axis=1)
    both = np.logical_or(columns, rows)

    if np.sum(both) == num_of_boards:
        state = np.isin(boards, draws[: i - 1])
        columns = state.all(axis=1).any(axis=1)
        rows = state.all(axis=2).any(axis=1)
        both = np.logical_or(columns, rows)

        called = np.isin(boards[~both], draws[:i])
        print(np.sum(boards[~both][~called]), draws[i - 1])
        break


## cool solution found from reddit, saving it here--
from numpy import loadtxt

n, *b = open(0)

n = loadtxt(n.split(",")).reshape(-1, 1, 1, 1)  # (numbers,1,1,1)
b = loadtxt(b).reshape(1, -1, 5, 5)  # (1,boards,5,5)

m = (n == b).cumsum(0)  # (numbers,boards,5,5)
s = (n * b * (1 - m)).sum((2, 3))  # (numbers,boards)
w = (m.all(2) | m.all(3)).any(2).argmax(0)  # (boards,)

print(s[w].diagonal()[w.argsort()[[0, -1]]])
