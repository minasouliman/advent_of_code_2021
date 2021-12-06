
import pandas as pd

def count_increasing(data: pd.Series) -> int:
    increasing = data.diff(1)
    return sum(increasing > 0)

# Part 1
data = pd.read_csv("input.csv")
print(count_increasing(data["depth"]))


# Part 2
count_increasing(data["depth"].rolling(window=3,min_periods=3).sum())
