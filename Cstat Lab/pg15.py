import numpy as np


rows = int(input("Enter no. of rows : "))
cols = int(input("Enter no. of cols : "))

arr = np.zeros((rows, cols), dtype = int)

for i in range(rows):
    for j in range(cols):
        arr[i, j] = int(input(f"Enter elements of ({i}, {j}) : "))

print(arr)

arr1d = arr.flatten()
print(arr1d)
