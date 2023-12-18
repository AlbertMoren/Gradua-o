'''Create a subroutine that calculates the greatest common divisor (GCD) of two numbers received as
parameters.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to get user input for the two numbers
def input_numbers():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a, b

# User inputs the data
num1, num2 = input_numbers()

# Calling the subroutine
gcd_result = calculate_gcd(num1, num2)

# Displaying the result
print(f"The greatest common divisor (MDC) of {num1} and {num2} is: {gcd_result}")
