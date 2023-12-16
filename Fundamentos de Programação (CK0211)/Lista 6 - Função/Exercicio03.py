'''Write a subroutine that takes two numbers as parameters and returns 0 if the first number is divisible by the second number. Otherwise, the next divisor must be returned.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def next_divisor_or_zero(num1, num2):
    if num1 % num2 == 0:
        return 0
    elif num2 > num1:
        return num1
    else:
        i = num2 + 1
        while num1 % i != 0:
            i += 1
        return i

# Input two numbers
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())

result = next_divisor_or_zero(num1, num2)

if result == 0:
    print(f"{num1} and {num2} are divisible.")
else:
    print(f"{num1} is divisible by the next divisor: {result}")
