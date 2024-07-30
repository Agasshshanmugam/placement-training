import numpy as np

matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

sum_matrix = matrix_a + matrix_b
product_matrix = np.dot(matrix_a, matrix_b)
transpose_matrix = np.transpose(matrix_a)

print("Matrix A:")
print(matrix_a)
print("Matrix B:")
print(matrix_b)
print("Sum of matrices:")
print(sum_matrix)
print("Product of matrices:")
print(product_matrix)
print("Transpose of Matrix A:")
print(transpose_matrix)
