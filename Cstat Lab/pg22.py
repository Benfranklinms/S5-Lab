import numpy as np


rows = int(input("Enter no. of rows : "))
cols = int(input("Enter no. of cols : "))

matrix = np.zeros((rows, cols), dtype = int)

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input("Enter no. of elements : "))

print("Matrix : ", matrix)

eigen_values, eigen_vectors = np.linalg.eig(matrix)

print("Eigen values : ", eigen_values)
print("Eigen vectors : ", eigen_vectors)

print(np.allclose(matrix @ eigen_vectors, eigen_vectors @ np.diag(eigen_values)))


#note for verification

#Verification (A @ v = λv): True
