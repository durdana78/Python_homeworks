import numpy as np
matrix = np.random.rand(5,5)
row_sums = np.sum(matrix, axis = 1)
col_sums = np.sum(matrix, axis = 0)

print(row_sums, col_sums)