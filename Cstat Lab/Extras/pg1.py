import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("test.txt", dtype = int)
print(data)

plt.hist(data, bins = 5, edgecolor = "black", color = "pink")
plt.show()
