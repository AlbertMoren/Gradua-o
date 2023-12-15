'''Create a program that fills a 6 X 3 matrix, calculates and shows:
■ the largest element of the matrix and its respective position, that is, row and column;
■ the smallest element of the matrix and its respective position, that is, row and column.'''

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

mat = create_matrix(6, 3, 0)
largest, row_largest, column_largest = 0, 0, 0
smallest, row_smallest, column_smallest = 0, 0, 0

for i in range(len(mat)):                       # Filling the matrix
    for j in range(len(mat[i])):
        mat[i][j] = randint(0, 30)
        if i == 0 and j == 0:
            smallest = mat[i][j]
        if mat[i][j] < smallest:
            smallest = mat[i][j]
            row_smallest = i
            column_smallest = j
        if mat[i][j] > largest:
            largest = mat[i][j]
            row_largest = i
            column_largest = j

for row in mat:                               # Print the matrix on the screen
    print("|", end='')  
    for value in row:
        print(f" {value:3} |", end=' ')
    print("")

print(f"The largest element is in row {row_largest + 1}, column {column_largest + 1}, and has the value {largest}")
print(f"The smallest element is in row {row_smallest + 1}, column {column_smallest + 1}, and has the value {smallest}")
