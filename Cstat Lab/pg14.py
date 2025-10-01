import numpy as np


rows = int(input("Enter no. of rows : "))
cols = int(input("Enter no. of cols : "))
depth = int(input("Enter depth : "))

arr = np.zeros((depth, rows, cols), dtype = int)

for k in range(depth):
    for i in range(rows):
        for j in range(cols):
            arr[k, i, j] = int(input(f"Element at ({k}, {i}, {j}) : "))


print("Original array is : ", arr)

def diagonal(arr):
    return {
        "axis 1-2" : np.diagonal(arr, axis1 = 1, axis2 = 2),
        "axis 0-1" : np.diagonal(arr, axis1 = 0, axis2 = 1),
        "axis 0-2" : np.diagonal(arr, axis1 = 0, axis2 = 2),
        }

diags = diagonal(arr)

for name, val in diags.items():
    print(name, val)
