'''Create a program that fills a 5 X 5 matrix with integers, calculates and displays the sum:
■ of the elements in line 4;
■ of the elements in column 2;
■ of the elements of the main diagonal;
■ of the elements of the secondary diagonal;
■ of all elements in the array'''

from random import randint

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

mat = create_matrix(5, 5, 0)
soma_linha_4 = 0
soma_coluna_2 = 0
soma_diagonal_principal = 0
soma_diagonal_secundaria = 0
total = 0

for i in range(len(mat)):                       # Filling the matrix
    for j in range(len(mat[i])):
        mat[i][j] = randint(0, 10)
        total += mat[i][j]

for row in mat:                               # Print the matrix on the screen
    print("|", end='')  
    for value in row:
        print(f" {value:3} |", end=' ')
    print("")

for i in range(len(mat)):
    soma_linha_4 += mat[3][i]

for i in range(len(mat)):
    soma_coluna_2 += mat[i][1]

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i == j:
            soma_diagonal_principal += mat[i][j]

for i in range(len(mat)):
    soma_diagonal_secundaria += mat[i][4 - i]

print(f"A soma total dos valores da matriz é {total}\nA soma da linha 4 = {soma_linha_4}\nA soma da coluna 2 = {soma_coluna_2}\nA soma da diagonal principal = {soma_diagonal_principal}\nA soma da diagonal secundária = {soma_diagonal_secundaria}")
