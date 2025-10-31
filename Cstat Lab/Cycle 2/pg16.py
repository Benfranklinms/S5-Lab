import numpy as np

def binet(n):
    root5 = np.sqrt(5)
    phi = (1 + root5) / 2
    psi = (1 - root5) / 2

    indices = np.arange(n)
    fib_series = (np.power(phi, indices) - np.power(psi, indices) / root5)

    return fib_series.astype(int)


num = 10
fib = binet(num)
print(fib)
