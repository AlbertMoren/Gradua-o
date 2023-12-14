# Program Description:
# This program presents a menu of options that allows the user to choose an operation.
# It receives the necessary data to perform the chosen operation and displays the result.
# It checks for the possibility of an invalid option, and it doesn't concern itself with constraints such as invalid salary.
#
# Menu options:
# 1. New salary
# 2. Vacation
# 3. Thirteenth salary
# 4. Exit
# Enter the desired option.
#
# For option 1: receive the salary of an employee, calculate and show the new salary using the following rules:
# SALARIES                                      | PERCENTAGE INCREASE
# Up to R$ 210.00                               | 15%
# From R$ 210.00 to R$ 600.00 (inclusive)       | 10%
# Above R$ 600.00                               | 5%
#
# For option 2: receive the salary of an employee, calculate and show the value of their vacation.
# Vacation is equal to their salary plus one-third of the salary.
#
# For option 3: receive the salary of an employee and the number of months worked in the company, up to twelve.
# Calculate and show the value of the thirteenth salary. The thirteenth salary is equal to their salary
# multiplied by the number of months worked divided by 12.
#
# For option 4: exit the program.

# Loop to process user input
while True:
    # Get user choice
    choice = int(input("Enter your choice (1-4): "))

    # Check user choice
    if choice == 1:
        # Option 1: New Salary
        current_salary = float(input("Enter current salary: "))
        # Calculate new salary based on rules
        if current_salary <= 210.00:
            new_salary = current_salary + (current_salary * 0.15)
        elif 210.00 < current_salary <= 600.00:
            new_salary = current_salary + (current_salary * 0.10)
        else:
            new_salary = current_salary + (current_salary * 0.05)
        print(f"The new salary is: {new_salary:.2f}")
    elif choice == 2:
        # Option 2: Vacation
        current_salary = float(input("Enter current salary: "))
        # Calculate vacation value
        vacation_value = current_salary + (current_salary / 3)
        print(f"The vacation value is: {vacation_value:.2f}")
    elif choice == 3:
        # Option 3: Thirteenth Salary
        current_salary = float(input("Enter current salary: "))
        months_worked = int(input("Enter the number of months worked (up to 12): "))
        # Calculate thirteenth salary
        thirteenth_salary = (current_salary * months_worked) / 12
        print(f"The thirteenth salary is: {thirteenth_salary:.2f}")
    elif choice == 4:
        # Option 4: Exit
        break
    else:
        print("Invalid option. Please enter a number between 1 and 4.")
