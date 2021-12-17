#%%
#target area: x=206..250, y=-105..-57

import numpy as np

grid = np.zeros((1000,1000))

target_x = (206,250)
target_y = (-105,-57)
# target_x = (20,30)
# target_y = (-10,-5)

maxs = {}

for i in range(19,1000):
    for j in range(-1000,1000):
        velocity = (i,j)

        hit = False
        missed = False
        position = (0,0)
        initial_velocity = velocity
        max_y = 0

        while (not hit) and (not missed):
            position = tuple(map(sum, zip(position, velocity)))
            velocity = (max(0,velocity[0]-1),velocity[1]-1)
            max_y = max(max_y,position[1])

            if (target_x[0] <= position[0] <= target_x[1]) & (target_y[0] <= position[1] <= target_y[1]):
                hit = True
                maxs[initial_velocity] = max_y
            if (position[0] >= target_x[1]) or (target_y[0] >= position[1]):
                missed = True

max_found = max(maxs, key=maxs.get)
print(max_found,maxs[max_found])
print(len(maxs))