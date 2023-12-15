'''Write a program that fills an 8 x 6 matrix of integers, calculates and displays the average of the elements
of the even rows of the matrix'''

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
matrix = create_matrix(8, 6, 0)

# Populate the matrix with random integer values
for i in range(8):
    for j in range(6):
        matrix[i][j] = random.randint(1, 100)  # Random integer values between 1 and 100

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Calculate and display the average of elements in even rows
even_row_sums = [sum(matrix[i]) for i in range(0, 8, 2)]
even_row_counts = [len(matrix[i]) for i in range(0, 8, 2)]
even_row_averages = [sum_row / count_row for sum_row, count_row in zip(even_row_sums, even_row_counts)]

print("\nAverage of elements in even rows:")
for i, avg in enumerate(even_row_averages):
    print(f"Row {2 * i + 1}: {avg:.2f}")