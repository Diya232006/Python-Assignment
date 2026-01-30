import numpy as np

# Input 5x3 matrix
print("Enter elements for 5x3 matrix:")
matrix_5x3 = []
for i in range(5):
    row = []
    for j in range(3):
        val = float(input(f"Element [{i+1},{j+1}]: "))
        row.append(val)
    matrix_5x3.append(row)
matrix_5x3 = np.array(matrix_5x3)

# Input 3x2 matrix
print("\nEnter elements for 3x2 matrix:")
matrix_3x2 = []
for i in range(3):
    row = []
    for j in range(2):
        val = float(input(f"Element [{i+1},{j+1}]: "))
        row.append(val)
    matrix_3x2.append(row)
matrix_3x2 = np.array(matrix_3x2)

# Product matrix
product = np.dot(matrix_5x3, matrix_3x2)

print("\nProduct Matrix (5x2):")
print(product)