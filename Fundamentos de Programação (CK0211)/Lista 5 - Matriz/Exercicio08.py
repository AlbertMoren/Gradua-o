'''Create a program that fills two 3 X 8 matrices with integers, calculates and displays:
■ the sum of the two matrices, resulting in a third matrix also of order 3 X 8;
■ the difference of the two matrices, resulting in a fourth matrix also of order 3 X 8'''

# My signature 
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

from random import randint

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

mat1 = create_matrix(3, 8, 0)

for i in range(len(mat1)):                       # Filling the first matrix
    for j in range(len(mat1[i])):
        mat1[i][j] = randint(0, 100)

mat2 = create_matrix(3, 8, 0)

for i in range(len(mat2)):                       # Filling the second matrix
    for j in range(len(mat2[i])):
        mat2[i][j] = randint(0, 100)

mat_result_sum = []
for i in range(len(mat1)):                      # Sum the matrices
    row = []
    for j in range(len(mat1[i])):
        row.append(mat1[i][j] + mat2[i][j])
    mat_result_sum.append(row)

for row in mat_result_sum:                               # Print the matrix on the screen
    print("|", end='')  
    for value in row:
        print(f" {value:3} |", end=' ')
    print("")

print("="*60)

mat_result_difference = []
for i in range(len(mat1)):                      # Subtract the matrices
    row = []
    for j in range(len(mat1[i])):
        if mat2[i][j] < 0:
            row.append(mat1[i][j] - (-mat2[i][j]))
        else:
            row.append(mat1[i][j] - mat2[i][j])
    mat_result_difference.append(row)

for row in mat_result_difference:                               # Print the matrix on the screen
    print("|", end='')  
    for value in row:
        print(f" {value:3} |", end=' ')
    print("")
