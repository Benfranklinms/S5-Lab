import numpy as np


rows = int(input("Enter no. of rows : "))
cols = int(input("Enter no. of cols : "))

arr = np.zeros((rows, cols), dtype = int)

for i in range(rows):
    for j in range(cols):
        arr[i][j] = int(input("Enter elements into array : "))

print("Original array : ", arr)

inverse = np.linalg.inv(arr)

print("Inverse of a matrix : ", inverse)
