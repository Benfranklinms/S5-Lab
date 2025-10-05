import numpy as np


arr = np.array(list(map(int, input("Enter elements in the array : ").split())))

n = int(input("Enter the order of difference : "))

difference = np.diff(arr, n = n)
print(difference)


#function use here is np.diff(arr, n = n)
