'''Write a program that fills a 5 x 5 matrix and creates two vectors of five positions each, which
contain, respectively, the sums of the rows and columns of the matrix. The program should write
the matrix and vectors created.'''

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
matrix = create_matrix(5, 3, 0)

# Populate the matrix with random values between 1 and 10
for i in range(5):
    for j in range(3):
        matrix[i][j] = random.randint(1, 10)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Create vectors for row sums and column sums
row_sums = [sum(row) for row in matrix]
column_sums = [sum(col) for col in zip(*matrix)]

# Display the vectors
print("\nRow Sums:")
print(row_sums)

print("\nColumn Sums:")
print(column_sums)
