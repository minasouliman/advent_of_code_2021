#%%
import csv
from typing import ByteString, List
from collections import Counter

insertions = {}

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        k, v = line[0].split(" -> ")
        insertions[k] = v

pattern = "OOBFPNOPBHKCCVHOBCSO"

pattern_dict = Counter()
for j in range(len(pattern) - 1):
    pattern_dict[pattern[j : j + 2]] += 1

print(pattern_dict)

for i in range(40):
    new_pattern_dict = Counter()
    for k in pattern_dict:
        new_pattern_dict[k[0] + insertions[k]] += pattern_dict[k]
        new_pattern_dict[insertions[k] + k[1]] += pattern_dict[k]
    pattern_dict = new_pattern_dict


first = Counter()
second = Counter()
for k in pattern_dict:
    first[k[0]] += pattern_dict[k]
    second[k[1]] += pattern_dict[k]

print(first,'\n',second)

print(first.most_common()[0][1], first.most_common()[-1][1])
print(second.most_common()[0][1], second.most_common()[-1][1])


"OBSO"

"OB"
"BS"
"SO"