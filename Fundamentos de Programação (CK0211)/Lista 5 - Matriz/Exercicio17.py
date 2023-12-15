'''Write a program that fills in and displays the average of the elements on the main diagonal of a matrix
10x10.'''

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
matrix = create_matrix(10, 3, 0)

# Populate the matrix with random values between 1 and 10
for i in range(10):
    for j in range(3):
        matrix[i][j] = random.randint(1, 10)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Calculate and display the average of the main diagonal elements
diagonal_sum = sum(matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))
average_diagonal = diagonal_sum / min(len(matrix), len(matrix[0]))

print(f"\nAverage of the main diagonal elements: {average_diagonal:.2f}")
