import numpy as np


a = np.array([[1,2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

kronecker_product = np.kron(a, b)

print("Matrix A : ", a)
print("Matrix B : ", b)
print(kronecker_product)
