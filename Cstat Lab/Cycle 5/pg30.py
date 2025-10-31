#Histogram for height of students in a class


import numpy as np
import matplotlib.pyplot as plt


height = np.array([158, 170, 190, 200, 160, 176, 177, 189])

plt.hist(height, bins = 5, edgecolor = "black", color = "pink")
plt.show()
