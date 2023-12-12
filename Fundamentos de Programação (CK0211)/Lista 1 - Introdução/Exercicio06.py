# A program that receives a fixed salary plus 4% commission on sales. It should receive the employee's fixed salary and the value of their sales, calculate and display the commission, and the final salary.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the fixed salary of the employee
fixed_salary = float(input("Enter the fixed salary: $"))

# Input the total sales value
sales = float(input("Enter the total sales: $"))

# Calculate the commission and final salary
commission = sales * 0.04
final_salary = fixed_salary + commission

# Print the commission and final salary
print(f"Commission: ${commission}")
print(f"Final salary: ${final_salary}")
