import numpy as np


def binet(n):
    sqrt5 = np.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2

    indices = np.arange(n)

    fib_series = (np.power(phi, indices) - np.power(psi, indices) / sqrt5)

    return np.rint(fib_series).astype(int)

num = 10
fib = binet(num)
print(fib)
