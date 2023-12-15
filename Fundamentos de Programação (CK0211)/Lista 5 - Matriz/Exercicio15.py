'''Create a program that fills a 12 x 13 matrix and divides all the elements in each row by the
largest element in module of that line. The program must write the read and modified matrix.'''

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

# Create and populate the matrix
matrix = create_matrix(12, 3, 0)

# Populate the matrix with random values between -50 and 50
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = random.randint(-50, 50)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Divide each element in a row by the absolute value of the maximum element in that row
for i in range(len(matrix)):
    max_abs_value = max(map(abs, matrix[i]))
    for j in range(len(matrix[i])):
        matrix[i][j] /= max_abs_value

# Display the modified matrix
print("\nModified Matrix:")
for row in matrix:
    print(row)
