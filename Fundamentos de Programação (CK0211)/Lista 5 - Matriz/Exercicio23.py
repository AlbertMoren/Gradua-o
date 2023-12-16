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
matrix = create_matrix(3, 4, 0)
'''Write a program that fills a 3 x 4 matrix, calculates and displays:
■ the number of even elements;
■ the sum of odd elements;
■ the average of all elements'''


# Populate the matrix with random integer values between 1 and 20
for i in range(3):
    for j in range(4):
        matrix[i][j] = random.randint(1, 20)

# Calculate the quantity of even elements, the sum of odd elements, and the average of all elements
even_count = 0
odd_sum = 0
total_elements = 0

for i in range(3):
    for j in range(4):
        if matrix[i][j] % 2 == 0:
            even_count += 1
        else:
            odd_sum += matrix[i][j]
        total_elements += 1

average = sum(sum(row) for row in matrix) / total_elements

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Display the results
print("\nResults:")
print(f"Quantity of Even Elements: {even_count}")
print(f"Sum of Odd Elements: {odd_sum}")
print(f"Average of All Elements: {average:.2f}")
