'''Create a program that fills a 2 X 4 matrix with integers and calculates and displays:
■ the number of elements between 12 and 20 in each line;
■ the average of the even elements of the matrix'''

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

mat = create_matrix(2, 4, 0)
total_sum = 0
line1_count = 0
line2_count = 0
even_count = 0

for i in range(len(mat)):                       # Filling the matrix
    for j in range(len(mat[i])):
        mat[i][j] = randint(0, 25)
                        
for row in mat:                               # Print the matrix on the screen
    print("|", end='')  
    for value in row:
        print(f" {value:3} |", end=' ')
    print("")
    
for i in range(len(mat)):                       # Business rules
    for j in range(len(mat[i])):
        if mat[i][j] % 2 == 0:
            total_sum += mat[i][j]
            even_count += 1
        if i == 0:
            if 12 < mat[i][j] < 20:
                line1_count += 1
        else:
            if 12 < mat[i][j] < 20:
                line2_count += 1
    
print(f"The average of the even elements in the matrix is {total_sum / even_count:.2f}\nElements between 12 and 20 are as follows\nIn line 1 = {line1_count} and in line 2 = {line2_count}")
