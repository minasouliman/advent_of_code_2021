#%%
import pandas as pd
import numpy as np

vertical_key = {"up": -1, "down": 1, "forward": 0}
horizontal_key = {"up": 0, "down": 0, "forward": 1}

data = pd.read_csv("input.csv", delimiter=" ")
data["vertical_directions"] = data.direction.map(vertical_key) * data["magnitude"]
data["horizontal_directions"] = data.direction.map(horizontal_key) * data["magnitude"]
print(np.prod(data[["vertical_directions","horizontal_directions"]].cumsum().iloc[-1].values))


data['aim'] = data["vertical_directions"].cumsum()
data['vertical_movement'] = data["horizontal_directions"] * data['aim']
print(np.prod(data[["vertical_movement","horizontal_directions"]].cumsum().iloc[-1].values))


