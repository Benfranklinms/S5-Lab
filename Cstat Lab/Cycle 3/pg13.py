import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = np.cos(x)

plt.plot(x, y)
plt.grid(True)
plt.show()
