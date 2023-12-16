'''Write a program that fills a 5 x 5 matrix of real numbers. Next, the program should
multiply each line by the main diagonal element of that line and show the matrix after the
multiplications.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

import random

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

# Create the desired matrix
matrix = create_matrix(5, 5, 0.0)

# Populate the matrix with random real values
for i in range(5):
    for j in range(5):
        matrix[i][j] = random.uniform(1.0, 10.0)  # Random real values between 1.0 and 10.0

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Multiply each row by the element of the main diagonal of that row
for i in range(5):
    diagonal_element = matrix[i][i]
    for j in range(5):
        matrix[i][j] *= diagonal_element

# Display the resulting matrix after the multiplications
print("\nResulting Matrix:")
for row in matrix:
    print(row)
