#%%
from types import TracebackType
import numpy as np
import csv

from numpy.core.fromnumeric import trace

REGEN_DAYS = 6
REGEN_DAYS_NEW = 8


with open("input.csv") as f:
    reader = csv.reader(f)
    fish = [int(i) for i in list(reader)[0]]

# Part 1
SIM_DAYS = 80


def simulate(counter, days):
    if days <= counter:
        return 1
    if counter == 0:
        return simulate(REGEN_DAYS, days - 1) + simulate(REGEN_DAYS_NEW, days - 1)
    if counter > 0:
        return simulate(counter - 1, days - 1)


print(sum([simulate(i, SIM_DAYS) for i in fish]))

# Part 2
SIM_DAYS = 256
from collections import Counter

tracker = Counter(fish)

for day in reversed(range(SIM_DAYS)):
    day_1 = tracker[1]
    for i in range(2, 9):
        tracker[i - 1] = tracker[i]
    tracker[8] = tracker[0]
    tracker[6] += tracker[0]
    tracker[0] = day_1

print(sum(tracker.values()))
