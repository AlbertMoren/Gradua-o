'''Create a program that fills a 4 x 5 matrix, calculates and displays a vector with five positions,
where each position contains the sum of the elements in each column of the matrix. The program should show
only elements of the vector greater than ten. If there is no element greater than ten, you must
show a message.'''

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
matrix = create_matrix(4, 3, 0)

# Populate the matrix with random integer values between 1 and 20
for i in range(4):
    for j in range(3):
        matrix[i][j] = random.randint(1, 20)

# Calculate the sum of each column
column_sums = [sum(col) for col in zip(*matrix)]

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Display only the elements of the vector greater than ten
print("\nColumn Sums Greater Than Ten:")
found = False
for i, column_sum in enumerate(column_sums):
    if column_sum > 10:
        print(f"Column {i + 1}: {column_sum}")
        found = True

# Display a message if no element is greater than ten
if not found:
    print("No column sum is greater than ten.")
