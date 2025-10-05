import numpy as np


def create_matrix():
    rows = int(input("Enter no. of rows : "))
    cols = int(input("Enter no. of cols : "))

    arr = np.zeros((rows, cols), dtype = int)

    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input("Enter no. of elements : "))

    return arr


a = create_matrix()
b = create_matrix()

corr_matrix = np.corrcoef(a, b)

print("Matrix A : ", a)
print("Matrix B : ", b)
print("Correlation coefficent : ", corr_matrix)
