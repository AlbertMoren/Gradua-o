'''Create a program that receives:
■ the grades of 15 students on five different tests and store them in a 15 x 5 matrix;
■ the names of the 15 students and store them in a 15-position vector.
The program should calculate and display:
■ for each student, the name, the arithmetic mean of the five tests and the status (passed, failed
or examination);
■ the class average'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

from random import uniform

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

mat = create_matrix(15, 5, 0)
names = ["alb","ert","sss","ggg","bbb","ccc","dd","ttt","ooo","xxx","zzz","hhh","qqqq","dddd","aaaa"]
averages = []
status = []

for i in range(len(mat)):
    total = 0                       # Filling the matrix
    for j in range(len(mat[i])):
        mat[i][j] = uniform(0, 10)
        total += mat[i][j]
    averages.append(total / 5)
    if averages[i] >= 7:
        status.append("Approved")
    elif 5 <= averages[i] < 7:
        status.append("Exam")
    else:
        status.append("Failed")

for i in range(len(averages)):                               # Print the matrix on the screen
    print(f"Student {names[i]:2} had an average of {averages[i]:.1f} and is {status[i]}")
