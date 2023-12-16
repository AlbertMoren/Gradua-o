'''Make a subroutine that receives an integer and positive value, calculates and displays its factorial'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def sub_routine(fat):
    if fat == 1:
        return fat
    else:
        return fat * sub_routine(fat - 1)

number = int(input("Enter a value: "))
print(f"The factorial of {number} = {sub_routine(number)}")
