'''Create a program that receives the salary of an employee and, using the following table, calculates and shows the new salary
SALARY RANGE          |% INCREASE
Up to R$ 300.00       |50%
R$ 300.00 R$ 500.00   |40%
R$ 500.00 R$ 700.00   |30%
R$ 700.00 R$ 800.00   |20%
R$ 800.00 R$ 1,000.00 |10%
Above R$ 1,000.00     |5%'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the employee's salary
salary = float(input("Enter your salary: R$"))

# Calculate the new salary based on the provided conditions
if salary <= 300.00:
    salary *= 1.5
elif 300.00 < salary <= 500.00:
    salary *= 1.4
elif 500.00 < salary <= 700.00:
    salary *= 1.3
elif 700.00 < salary <= 800.00:
    salary *= 1.2
elif 800.00 < salary <= 1000.00:
    salary *= 1.1
else:
    salary *= 1.05

# Display the result
print(f"Your new salary will be R${salary:.2f}")
