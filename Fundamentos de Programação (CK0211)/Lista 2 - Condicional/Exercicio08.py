'''Create a program to calculate and display the adjusted salary of an employee. The percentage increase is in the following table:
SALARY          PERCENTAGE INCREASE
Up to R$300.00  35%
Above R$300.00  15%
'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the salary
salary = float(input("Enter the salary: R$"))

# Check the salary range and calculate the adjusted salary accordingly
if salary <= 300:
    adjusted_salary = salary + (salary * 0.35)
else:
    adjusted_salary = salary + (salary * 0.15)

# Display the result
print(f"Your new salary will be R${adjusted_salary:.2f}")
