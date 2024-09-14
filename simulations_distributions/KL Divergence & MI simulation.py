#KL Divergence & MI (Mutual Information) Simulation
import numpy as np

# Given count data (generate this from table in the problem/example to work with...)
counts = np.array([[12, 11, 7],
                   [11, 15, 6],
                   [10, 12, 9],
                   [7, 9, 10]])

# Total count
n_total = np.sum(counts)

# Joint probability distribution f_{X,Y}(x,y)
f_XY = counts / n_total


# Compute marginal probabilities
f_X = np.sum(f_XY, axis=1)  # Sum over rows
f_Y = np.sum(f_XY, axis=0)  # Sum over columns
