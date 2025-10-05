import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

Q, R = np.linalg.qr(a)

print(Q)
print(R)

print(np.allclose(a, Q @ R))
