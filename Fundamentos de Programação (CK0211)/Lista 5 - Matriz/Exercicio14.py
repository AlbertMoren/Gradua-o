'''Write a program that fills a 2 x 3 matrix, calculates and displays the number of elements in the matrix that do not belong to the range [5,15].'''

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
matrix = create_matrix(2, 3, 0)

# Populate the matrix with random values between 1 and 20
for i in range(2):
    for j in range(3):
        matrix[i][j] = random.randint(1, 20)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Count and display the number of elements outside the interval [5, 15]
lower_bound = 5
upper_bound = 15
count_outside_interval = 0
for row in matrix:
    for element in row:
        if element < lower_bound or element > upper_bound:
            count_outside_interval += 1

print(f"\nNumber of elements outside the interval [{lower_bound}, {upper_bound}]: {count_outside_interval}")
