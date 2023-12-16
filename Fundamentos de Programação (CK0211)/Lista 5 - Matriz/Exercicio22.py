'''Create a program that fills in a 6 3 10 matrix, adds the columns individually and accumulates the sums in the 7th row of the matrix. The program should show the result for each column.'''

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
matrix = create_matrix(7, 3, 0)

# Populate the matrix with random integer values between 1 and 10
for i in range(6):
    for j in range(3):
        matrix[i][j] = random.randint(1, 10)

# Sum each column individually and accumulate the sums in the 7th row
for j in range(3):
    column_sum = sum(matrix[i][j] for i in range(6))
    matrix[6][j] = column_sum

# Display the original matrix with column sums
print("Matrix with Column Sums:")
for i in range(7):
    print(matrix[i])

# Display the result of each column
print("\nResult of Each Column:")
for j in range(3):
    print(f"Column {j + 1} Sum: {matrix[6][j]}")
