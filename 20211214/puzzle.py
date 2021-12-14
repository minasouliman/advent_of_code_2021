#%%
import csv
from typing import List
from collections import Counter

insertions = {}

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        k, v = line[0].split(" -> ")
        insertions[k] = v

pattern = "NNCB"
pattern_dict = Counter()
for j in range(len(pattern) - 1):
    pattern_dict[pattern[j : j + 2]] = 1


for i in range(40):
    new_pattern_dict = Counter()
    for k in pattern_dict:
        new_pattern_dict[k[0] + insertions[k]] = 1
        new_pattern_dict[insertions[k] + k[1]] = 1
    pattern_dict = pattern_dict + new_pattern_dict

print(pattern_dict)
