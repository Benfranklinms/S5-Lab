import numpy as np
import matplotlib.pyplot as plt


def create_matrix():
    rows = int(input("Enter no. of rows : "))
    cols = int(input("Enter no. of cols : "))

    arr = np.zeros((rows, cols), dtype = int)

    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input("Enter no. of elements : "))

    return arr


a = create_matrix()


plt.plot(a)
plt.grid(True)
plt.show()
