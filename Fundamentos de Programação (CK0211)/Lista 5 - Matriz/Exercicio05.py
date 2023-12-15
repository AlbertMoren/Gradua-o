'''Create a program that fills a 12 X 4 matrix with the sales values ​​of a store, where each line represents a month of the year and each column represents a week of the month. The program should calculate and display:
■ the total sold in each month of the year, showing the name of the month in full;
■ the total sold each week throughout the year;
■ the total sold by the store in the year.'''

#minha assinatura 
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

mat = create_matrix(12, 4, 0)
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
sales = []
total = 0 

for i in range(len(mat)):       # Filling the matrix and business rules
    total_month = 0
    for j in range(len(mat[i])):
        mat[i][j] = uniform(0, 5000)
        total_month += mat[i][j]
    sales.append(total_month)
    total += total_month

print("="*30)                   # Print report
for i in range(len(sales)):
    print(f"{months[i]} | $ {sales[i]:.2f}")

print("="*30)
for i in range(len(mat)):       # Print report
    total_week = 0
    for j in range(len(mat[i])):
        total_week += mat[i][j]
        print(f" {months[i]} in week {j+1} sold $ {total_week:.2f}")

print("="*30, f"\nIn this year, the store sold $ {total:.2f}")
