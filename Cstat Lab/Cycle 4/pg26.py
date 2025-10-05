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

mean = np.mean(a)
var = np.var(a)
std = np.std(a)

print("Mean : ", mean)
print("Variance : ", var)
print("Standard deviation : ", std)
