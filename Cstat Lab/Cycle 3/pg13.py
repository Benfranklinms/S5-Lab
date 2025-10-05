import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-10, 10, 200)
y = np.sin(x)

plt.plot(x, y)
plt.grid(True)
plt.show()
