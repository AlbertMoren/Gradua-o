from random import randint
'''Create a program that fills a 3 x 5 matrix with integers, calculates, and shows the quantity of elements between 15 and 20.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Function that generates a matrix
def create_matrix(n_rows, n_columns, value):
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)  # place the row in the matrix
        matrix.append(row)	
    return matrix

matrix = create_matrix(3, 5, 0)
count = 0

for i in range(len(matrix)):  # Validate the business rule
    for j in range(len(matrix[i])):
        matrix[i][j] = randint(10, 25)
        if 15 < matrix[i][j] < 20:
            count += 1

print(matrix)
print(f"There are {count} elements between 15 and 20.")
