import numpy as np


def create_matrix():
    rows = int(input("Enter no. of rows : "))
    cols = int(input("Enter no. of cols : "))
    arr = np.zeros((rows, cols), dtype = int)
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input("Enter elements into the array : "))
    return arr


a = create_matrix()
b = create_matrix()

expr = input("Enter an expression : ").replace(" ", "")

summation = np.einsum(expr, a, b)
print(summation)
