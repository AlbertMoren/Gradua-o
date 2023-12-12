'''Create a program that receives the number of hours worked, the value of the minimum wage, and the number of overtime hours worked, calculates and shows the salary to be received, according to the following rules:
a) the regular hour is worth 1/8 of the minimum wage;
b) the overtime hour is worth 1/4 of the minimum wage;
c) the gross salary is equal to the number of regular hours worked multiplied by the value of a regular hour;
d) the amount to receive for overtime hours is equal to the number of overtime hours worked multiplied by the value of an overtime hour;
e) the total salary to be received is equal to the gross salary plus the amount to receive for overtime hours.'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

salary = float(input("Enter the minimum wage: "))
hours_worked = float(input("Enter the number of regular hours worked: "))
overtime_hours = float(input("Enter the total number of overtime hours worked: "))

regular_salary = (1/8) * salary * hours_worked
total_salary = regular_salary + (1/4) * salary * overtime_hours

print(f"The total salary to be received is: {total_salary:.2f}")
