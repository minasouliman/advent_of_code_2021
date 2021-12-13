#%%
import csv
from typing import List

network = {}

with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        k, v = line[0].split("-")

        if (k in network) and (v != 'start'):
            network[k].append(v)
        if (v in network) and (k != 'start'):        
            network[v].append(k)
        if (k not in network) and (v != 'start'):
            network[k] = [v]
        if (v not in network) and (k != 'start'):
            network[v] = [k]



paths = []


def traverse(node, path=None, parent_node = None):
    if type(node) == list:
         [traverse(n, path) for n in node]
    elif node == "start":
        return traverse(network[node], "start")
    elif node not in network:
        if node == "end":
            paths.append(f"{path},end")
        elif node.islower():
            return None
        else:
            return traverse(network[node], f"{path},{network[node]}")
    else:
        traverse(network[node], f"{path},{node}", node)

print(network)
traverse("start")
# paths
