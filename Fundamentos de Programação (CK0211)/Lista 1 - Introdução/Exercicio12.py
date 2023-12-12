# A program that receives the value of the minimum wage and the salary of an employee, calculates and displays the quantity of minimum wages that the employee earns.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the values for the minimum wage and the employee's salary
salarioMinimo = float(input(print("Enter the minimum wage")))
salario = float(input(print("Enter the employee's salary")))

# Calculate the number of minimum wages the employee earns
salarios = salario // salarioMinimo

# Print the result
print(f"The employee earns {salarios} minimum wages.")
