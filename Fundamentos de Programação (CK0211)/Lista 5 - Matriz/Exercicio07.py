'''Create a program that fills a matrix M of order 4 X 6 and a second matrix N of order 6.'''
from random import randint

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

from random import randint

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

mat1 = create_matrix(4, 6, 0)
column_sum = []
row_sum = []
result_vector = []

for i in range(len(mat1)):                       # Filling the first matrix
    for j in range(len(mat1[i])):
        mat1[i][j] = randint(0, 100)

mat2 = create_matrix(6, 4, 0)

for i in range(len(mat2)):                       # Filling the second matrix
    for j in range(len(mat2[i])):
        mat2[i][j] = randint(0, 100)

for i in range(len(mat1)):                       # Summing the rows
    row_sum.append(sum(mat1[i]))

for i in range(len(mat2[i])):                     # Summing the columns
    column_sum.append(sum(mat1[j][i] for j in range(len(mat1))))

for i in range(len(row_sum)):                  # Summing the rows and columns
    result_vector.append(row_sum[i] + column_sum[i])

for value in result_vector:
    print(f"{value:2} ", end='')
