'''Create a subroutine that receives two values X and Z as parameters, calculates and returns Xz without using
ready-made functions or power operators.'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def calculate_power(x, z):
    result = 1

    for _ in range(z):
        result *= x

    return result

# Input the values of X and Z
x = int(input("Enter the value of X: "))
z = int(input("Enter the value of Z: "))

# Calculate and print X^Z
result_power = calculate_power(x, z)
print(f"{x}^{z} is: {result_power}")
