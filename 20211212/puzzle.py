#%%
import csv
from typing import List

network = {}

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        k, v = line[0].split("-")

        if (k in network) and (v != "start"):
            network[k].append(v)
        if (v in network) and (k != "start"):
            network[v].append(k)
        if (k not in network) and (v != "start"):
            network[k] = [v]
        if (v not in network) and (k != "start"):
            network[v] = [k]


paths = []


def traverse(node, path=None, single_small=False):
    if node == "start":
        return traverse(network[node], "start", single_small)
    elif node == "end":
        paths.append(f"{path},end")
    elif type(node) == list:
        [traverse(n, path, single_small) for n in node]
    elif node.islower() & ((path.count(node) > 0) & single_small):
        return None
    elif node.islower() & (path.count(node) == 1):
        traverse(network[node], f"{path},{node}", True)
    else:
        traverse(network[node], f"{path},{node}", single_small)


print(network)
traverse("start")
print(paths)
len(paths)
