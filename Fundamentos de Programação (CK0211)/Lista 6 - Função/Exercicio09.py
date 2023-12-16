'''Create a subroutine that takes a positive integer value as a parameter and returns the sum of the divisors of that value.'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def sub_routine(number, i):
    if i == number:
        return number
    else:
        if number % i == 0:
            return i + sub_routine(number, i + 1)
        else:
            return sub_routine(number, i + 1)

i = 1
number = int(input("Enter a value: "))
print(f"The sum of divisors of {number} = {sub_routine(number, i)}")
