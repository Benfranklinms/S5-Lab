import numpy as np

arr = np.arange(27).reshape(3, 3, 3)
print(arr)

diagonals = np.diagonal(arr, axis1 = 1, axis2 = 2)
print(diagonals)
