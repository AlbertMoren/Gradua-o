'''Make a subroutine that takes an integer value and checks whether it is positive or negative.'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def check_number(n):
    if isinstance(n, (int, float)):
        if n > 0:
            print("This number is positive.")
        elif n == 0:
            print("This number is neutral.")
        else:
            print("This number is negative.")
    else:
        print("Invalid input. Please enter a valid number.")

# Get user input
user_input = input("Enter a number: ")

# Try to convert the input to a number
try:
    number = float(user_input)
    check_number(number)
except ValueError:
    print("Invalid input. Please enter a valid number.")
