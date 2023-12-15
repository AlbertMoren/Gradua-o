'''Write a program that fills a 3 x 3 matrix with real numbers and another numeric value entered by the user. The program must calculate and display the matrix resulting from multiplying the number entered by each element of the matrix.'''
from random import uniform,randint

# My signature 
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

from random import uniform, randint

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

mat = create_matrix(3, 8, 0)
mat_result = []

for i in range(len(mat)):                       # Filling the matrix
    for j in range(len(mat[i])):
        mat[i][j] = uniform(0, 100)

number = randint(1, 100)

for i in range(len(mat)):                       # Multiplying the elements of the matrix by a single value
    row = []
    for j in range(len(mat[i])):
        row.append(mat[i][j] * number)
    mat_result.append(row)

for row in mat_result:                                # Print the matrix on the screen
    print("|", end='')  
    for value in row:
        print(f" {value:.1f} |", end=' ')
    print("")
