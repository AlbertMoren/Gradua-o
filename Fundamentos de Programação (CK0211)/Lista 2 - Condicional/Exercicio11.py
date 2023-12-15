'''Create a program that receives the current salary of an employee and, using the following table, calculates and shows the value of the increase and the new salary.

SALARY             | INCREASE PERCENTAGE
Up to R$ 300.00    | 15%
R$ 300.00 R$ 600.00 | 10%
R$ 600.00 R$ 900.00 | 5%
Above R$ 900.00    | 0%
'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the current salary
salary = float(input("Enter your salary: R$"))

# Check the salary range and calculate the new salary accordingly
if salary <= 300.00:
    salary *= 1.15
elif 300.00 < salary <= 600.00:
    salary *= 1.10
elif 600.00 < salary <= 900.00:
    salary *= 1.05
else:
    # For salaries above 900.00, there is no increase
    salary *= 1.00

# Display the result
print(f"Your new salary will be R${salary:.2f}")
