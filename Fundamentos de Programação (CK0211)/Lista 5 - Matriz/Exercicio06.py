'''Write a program that fills a 20 X 10 matrix with integers, and adds each of the columns, storing the result of the sum in a vector. Next, the program must multiply each element of the matrix by the column sum and display the resulting matrix.'''

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

mat = create_matrix(20, 10, 0)
mat_result = []
column_sum = []

for i in range(len(mat)):                       # Filling the matrix
    for j in range(len(mat[i])):
        mat[i][j] = randint(0, 100)

for i in range(len(mat[i])):                       # Applying business rules
    total_sum =  0                      
    for j in range(len(mat)):
        total_sum += mat[j][i]
    column_sum.append(total_sum)

for i in range(len(mat[i])):
    row = []                       # Filling the matrix
    for j in range(len(mat)):
        row.append(mat[j][i] * column_sum[i])
    mat_result.append(row)

for row in mat_result:                               # Print the matrix on the screen
    print("|",end='')  
    for value in row:
        print(f" {value:0} |",end=' ')
    print("")