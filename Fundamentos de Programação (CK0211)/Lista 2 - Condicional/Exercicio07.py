'''A company decides to give a 30% raise to employees with salaries below R$ 500.00. Create a program that receives the employee's salary and shows the adjusted salary or a message if they are not eligible for the increase.'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the salary
salary = float(input("Enter the salary: R$"))

if salary <= 500:
    print(f"Your new salary will be {(salary + (salary * 0.3)):.2f}")
else:
    print("You are not eligible for a raise")
