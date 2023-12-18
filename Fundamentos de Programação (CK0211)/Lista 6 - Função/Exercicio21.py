'''Make a subroutine that receives a 10X10 matrix and determines the largest element above the diagonal
main. This value should be shown in the main program.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

import random

def create_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def find_largest_above_diagonal(matrix):
    largest_element = float('-inf')

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            if matrix[i][j] > largest_element:
                largest_element = matrix[i][j]

    return largest_element

# Create a 10x10 matrix using the create_matrix function
matrix = create_matrix(10, 10)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Call the subroutine
largest_element = find_largest_above_diagonal(matrix)

# Display the result
print(f"\nThe largest element above the main diagonal is: {largest_element}")
