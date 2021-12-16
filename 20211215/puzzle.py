#%%
import numpy as np
import csv
import networkx as nx


grid = []
with open("input.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        grid.append(list(map(int, list(line[0]))))

grid = np.array(grid)
new_grid = grid

for i in range(4):
    grid = (grid + 1) % 10
    grid[grid == 0] = 1
    new_grid = np.append(new_grid, grid, axis=1)

grid = new_grid
for i in range(4):
    grid = (grid + 1) % 10
    grid[grid == 0] = 1
    new_grid = np.append(new_grid, grid, axis=0)

np.savetxt("input_expanded.csv", new_grid.astype(int),fmt='%i',delimiter='')

G = nx.grid_2d_graph(500,500)
D = nx.MultiDiGraph()
D.add_nodes_from(G.nodes)
D.add_edges_from(G.edges)
D.add_edges_from([(j,i) for i,j in G.edges])

with open("input_expanded.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        for j,v in enumerate(list(map(int,list(line[0])))):
            for nbr in D[(i,j)]:
                D.edges[nbr,(i,j),0]['weight'] = v

shortest_path = nx.dijkstra_path(D,(0,0),(499,499),weight="weight")
nx.path_weight(D,shortest_path,weight="weight")
