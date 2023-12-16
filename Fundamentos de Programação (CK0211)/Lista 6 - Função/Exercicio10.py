'''Create a subroutine that receives two values X and Z as parameters, calculates and returns X^Z without using ready-made functions or power operators.'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def sub_routine(x, z):
    if z == 1:
        return x
    else:
        return x * sub_routine(x, z - 1)

number1, number2 = map(int, input("Enter two values: ").split(" "))
print(f"{number1} raised to the power of {number2} = {sub_routine(number1, number2)}")