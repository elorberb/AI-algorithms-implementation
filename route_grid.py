import numpy as np
import pandas as pd

def create_grid(grid_num=1):
    if grid_num == 1:
        with open("grid_1", "rt") as infile:
            return np.matrix([list(line.strip()) for line in infile.readlines()]), (0, 0), (16, 4)
    if grid_num == 2:
        with open("grid_2", "rt") as infile:
            return np.matrix([list(line.strip()) for line in infile.readlines()]), (0, 0), (138, 138)

# grid , s ,e = create_grid(grid_num=2)
# print(grid[0,0])