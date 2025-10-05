import numpy as np


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

inner = np.inner(a, b)
outer = np.outer(a, b)
cross = np.cross(a, b)

print("Inner : ", inner)
print("Outer : ", outer)
print("Cross : ", cross)
