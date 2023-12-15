'''Create a program that: fills a 6 3 4 matrix; recalculate the entered matrix, where each line must be multiplied by the largest element of the line in question; show the resulting matrix.'''

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
matrix = create_matrix(6, 3, 0)

# Populate the matrix with random values between 1 and 10
for i in range(6):
    for j in range(3):
        matrix[i][j] = random.randint(1, 10)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Recalculate the matrix by multiplying each row by its maximum element
for i in range(len(matrix)):
    max_value = max(matrix[i])
    for j in range(len(matrix[i])):
        matrix[i][j] *= max_value

# Display the resulting matrix
print("\nResulting Matrix:")
for row in matrix:
    print(row)
