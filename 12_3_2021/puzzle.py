#%%
import pandas as pd
import numpy as np

converters = {"bit": lambda x: str(x)}
data = pd.read_csv("input.csv", converters=converters)
data = data.bit.str.split("", expand=True).replace('',np.nan).dropna(axis=1, how="all")

# Part 1
most_common = "".join(data.mode().values[0])
gamma = int(most_common, 2)
least_common = "".join([str(int(i != "1")) for i in most_common])
eps = int(least_common, 2)

print(f"gamma={gamma} --- epsilon={eps} --- power={gamma*eps}")

# Part 2
data_g = data.copy()
data_e = data.copy()

for col in data:
    if len(data_g) > 1:
        mode = data_g[col].mode().values[-1]
        data_g = data_g[data_g[col] == mode]
    if len(data_e) > 1:
        mode = data_e[col].mode().values[-1]
        data_e = data_e[data_e[col] == str(int(mode != "1"))]

most_common = "".join(data_g.values[0])
o2 = int(most_common, 2)

least_common = "".join(data_e.values[0])
co2 = int(least_common, 2)

print(f"o2={o2} --- co2={co2} --- power={o2*co2}")

