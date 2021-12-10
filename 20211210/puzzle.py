#%%
import numpy as np
import csv

data = []

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        data.append(line[0])

legal = ["<>", "[]", "{}", "()"]
legal_closing = [">", "]", "}", ")"]
legal_closing_values = [25137, 57, 1197, 3]


def get_illegal(line):
    line_len = np.inf
    while len(line) < line_len:
        line_len = len(line)
        for pair in legal:
            line = line.replace(pair, "")

    illegals_found = [line.find(i) if i in line else np.inf for i in legal_closing]
    if sum([i == np.inf for i in illegals_found]) == 4:
        return 0
    first_illegal = illegals_found.index(min(illegals_found))

    return legal_closing_values[first_illegal]


illegals = [get_illegal(i) for i in data]
print(illegals)
sum(illegals)

# part 2

complete_closing_value = {"(": 1, "[": 2, "{": 3, "<": 4}


def fix_incomplete(line):
    line_len = np.inf
    while len(line) < line_len:
        line_len = len(line)
        for pair in legal:
            line = line.replace(pair, "")

    line_rev = list(line[::-1])
    line_values = [complete_closing_value[i] for i in line_rev]
    val = 0
    for v in line_values:
        val = val * 5 + v
    return val


completion_scores = []

for i, v in enumerate(illegals):
    if v == 0:
        completion_scores.append(fix_incomplete(data[i]))


np.median(np.array(completion_scores))
