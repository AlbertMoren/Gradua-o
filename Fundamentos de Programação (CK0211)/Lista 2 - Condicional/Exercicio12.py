'''Create a program that receives the gross salary of an employee and, using the following table, calculates and shows the value to receive. It is known that this is composed of the gross salary plus gratuity and deducted 7% tax on the salary.

    GRATUITY TABLE
SALARY             | GRATUITY
Up to R$ 350.00   | R$ 100.00
R$ 350.00 R$ 600.00 | R$ 75.00
R$ 600.00 R$ 900.00 | R$ 50.00
Above R$ 900.00    | R$ 35.00
'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the gross salary
salary = float(input("Enter your salary: R$"))

# Check the salary range and calculate the gratuity accordingly
if salary <= 350.00:
    salary += 100.00
elif 350.00 < salary <= 600.00:
    salary += 75.00
elif 600.00 < salary <= 900.00:
    salary += 50.00
else:
    salary += 35.00

# Deduct 7% tax
salary *= 0.93

# Display the result
print(f"Your net salary will be R${salary:.2f}")
